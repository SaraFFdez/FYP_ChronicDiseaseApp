import spacy
import helpers

def create_training_data(data, type):
    patterns = []
    for item in data:
        pattern = {
            "label": type,
            "pattern": item 
            #"id": item   
        }
        patterns.append(pattern)
    return patterns

def save_entity_ruler():
    nlp = spacy.load("en_core_web_sm")
    config = {
        "phrase_matcher_attr": "LOWER",
        "validate": True,
        "overwrite_ents": False,
        "ent_id_sep": "||",
    }
    ruler = nlp.add_pipe("entity_ruler", config=config, after="ner")
    # symptoms_data = helpers.load_data("Backend\\AudioProcessing\\trainingData\\symptoms_data.json")
    # patterns_old = create_training_data(symptoms_data, "SYMPTOM")
    patterns = helpers.load_data("Backend\\AudioProcessing\\trainingData\\symptoms_patterns.json")
    ruler.add_patterns(patterns)
    #ruler.to_disk("Backend\\AudioProcessing\\trained_algorithms\\entity_ruler")

def symptoms_identifier(text):
    nlp = spacy.load("en_core_web_sm") #load pretrained nlp model
    ruler = nlp.add_pipe("entity_ruler", after="ner") #create entity ruler
    ruler.from_disk("Backend\\AudioProcessing\\trained_algorithms\\entity_ruler")
    doc = nlp(text)
    symptoms_found_id = []
    for ent in doc.ents:
        print (ent.text, ent.label_, ent.ent_id_)
        if ent.label_ == "SYMPTOM":
            if ent.ent_id_ not in symptoms_found_id:
                symptoms_found_id.append(ent.ent_id_)   
    return symptoms_found_id

test_text_Sukhi = "So today I woke up with a really intense headache where I just had really bad sensitivity to light and I just really felt like I was physically too fatigued to move. So I stayed in bed for about and extra hour today and an hour more than usual. So that brings my total sleep from eight to 9 hours. So roughly about 9 hours of sleep. Other symptoms include I've noticed my allergies a little bit today, so it just kind of stuff. He knows, maybe feeling a little bit ill, but that could just be from my allergies. So I'm not too sure in regards to meals, I just had some eggs in the morning, I had a smoothie and I drank water and I've just now recently had a coffee and for dinner or I'm going to have some chicken. In regards to activities, so I just sort of walked around my bike to work today, which is really good. So that's about five kilometres and I didn't think I'd be able to do that given how tired it was when I woke up and I don't think I have the energy to bike home, so I'm just going to walk to the train station and home. So Yeah."
print("LIST OF SYMPTOMS", symptoms_identifier(test_text_Sukhi))

