import spacy
import AudioProcessing.helpers as helpers
import numpy as np

#save any modifications to the entity ruler (from the expected files)
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

    processed_text = text.replace(" but ", ". ")
    doc = nlp(processed_text) #process the text
    symptoms_found_id = []

    for ent in doc.ents: #find symptoms entities and add them to a list if they are not repeated.
        if ent.label_ == "SYMPTOM": #check it is a symptom
            if text_classifier_symptoms(ent.sent.text): #check the phrase is "positive"
                #handle patterns
                if ent.ent_id_ == "pain_noun" or ent.ent_id_ == "pain_verb" or ent.ent_id_ == "noun_pain":
                    symptomID = pain_pattern_handler(ent)
                elif ent.ent_id_ == "sensitivity":
                    symptomID = sensitivity_pattern_handler(ent)
                else:
                    symptomID = ent.ent_id_
                #add to the symptoms list if not there yet
                if symptomID != "Error" and symptomID not in symptoms_found_id:
                    symptoms_found_id.append(symptomID) 
                      
    return symptoms_found_id

def text_classifier_symptoms(sentence, model_dir = 'Backend\\AudioProcessing\\trained_algorithms\\ML\\symptoms_classif_model'):
    nlpClassify = spacy.load(model_dir) #load model
    doc = nlpClassify(sentence) #process sentence
    max_confidence_label = list(doc.cats.keys())[np.argmax(np.array(list(doc.cats.values())))] #find label

    if max_confidence_label == "NEGATIVE":
        return False
    return True

#handle the different pain patterns
def pain_pattern_handler(ent):
    if ent.ent_id_ == "pain_noun" or ent.ent_id_ == "noun_pain":
        for word in ent:
            if word.pos_ == "NOUN" and word.lower_ != "pain":
                return word.lemma_ + " pain"
    elif ent.ent_id_ == "pain_verb":
        for word in ent:
            if word.pos_ == "NOUN" and word.lower_ != "pain":
                return "pain during " + word.lemma_
        for word in ent:
            if word.pos_ == "VERB":
                return "pain " + word.lemma_  
    return "Error"

#handle the different sensitivity patterns
def sensitivity_pattern_handler(ent):
    for word in ent:
        if word.pos_ == "NOUN" and word.lower_ != "sensitivity":
            return word.lemma_ + " sensitivity" 
    for word in ent:
        if word.lower_ != "sensitivity":
            return word.lemma_ + " sensitivity"
    return "unidentified sensitivity"

#save_entity_ruler()