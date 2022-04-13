import spacy
import helpers

def save_entity_ruler():
    nlp = spacy.load("en_core_web_sm")
    config = {
        "phrase_matcher_attr": "LOWER",
        "validate": True,
        "overwrite_ents": False,
        "ent_id_sep": "||",
    }
    ruler = nlp.add_pipe("entity_ruler", config=config, after="ner")
    patterns = helpers.load_data("Backend\\AudioProcessing\\trainingData\\symptoms_patterns.json")
    ruler.add_patterns(patterns)
    ruler.to_disk("Backend\\AudioProcessing\\trained_algorithms\\entity_ruler")

def symptoms_identifier(text):
    nlp = spacy.load("en_core_web_sm") #load pretrained nlp model
    ruler = nlp.add_pipe("entity_ruler", after="ner") #create entity ruler
    ruler.from_disk("Backend\\AudioProcessing\\trained_algorithms\\entity_ruler") #load entity ruler
    doc = nlp(text)
    symptoms_found_id = []

    for ent in doc.ents: #find symptoms entities and add them to a list if they are not repeated.
        print (ent.text, ent.label_, ent.ent_id_) #delete later
        if ent.label_ == "SYMPTOM":
            if ent.ent_id_ == "pain_noun" or ent.ent_id_ == "pain_verb" or ent.ent_id_ == "noun_pain":
                symptomID = pain_pattern_handler(ent)
            elif ent.ent_id_ == "sensitivity":
                symptomID = sensitivity_pattern_handler(ent)
            else:
                symptomID = ent.ent_id_

            if symptomID != "Error" and symptomID not in symptoms_found_id:
                symptoms_found_id.append(symptomID)   

    return symptoms_found_id

def pain_pattern_handler(ent):
    if ent.ent_id_ == "pain_noun" or ent.ent_id_ == "noun_pain":
        for word in ent:
            if word.pos_ == "NOUN" and word.lower_ != "pain":
                return word.text + " pain"
    elif ent.ent_id_ == "pain_verb":
        for word in ent:
            if word.pos_ == "NOUN" and word.lower_ != "pain":
                return "pain during " + word.text
        for word in ent:
            if word.pos_ == "VERB":
                return "pain " + word.text  
    return "Error"

def sensitivity_pattern_handler(ent):
    for word in ent:
        if word.pos_ == "NOUN" and word.lower_ != "sensitivity":
            return word.text + " sensitivity" 
    for word in ent:
        if word.lower_ != "sensitivity":
            return word.text + " sensitivity"
    return "unidentified sensitivity"

# for i in range(0,5):
#     text = helpers.audio_tests(i)
#     print(text)
#     print("LIST OF SYMPTOMS", symptoms_identifier(text))
text =  "The next day I woke up with the worst sore throat and felt sick overall, but I just kept going, thinking I would get better the next day. I developed bad vertigo, and also had fatigue and sleep problems. I went to the school health clinic and had a lot of tests done. All my tests came back fine— only months later I was found to have mononucleosis."
print(text)
print("LIST OF SYMPTOMS", symptoms_identifier(text))

#save_entity_ruler()
