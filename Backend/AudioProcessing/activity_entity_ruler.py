import spacy
from yaml import load
import helpers

def save_entity_ruler_activity():
    nlp = spacy.load("en_core_web_sm")
    config = {
        "phrase_matcher_attr": "LOWER",
        "validate": True,
        "overwrite_ents": False,
        "ent_id_sep": "||",
    }
    ruler = nlp.add_pipe("entity_ruler", config=config, after="ner")
    patterns = helpers.load_data("Backend\\AudioProcessing\\trainingData\\activity_patterns.json")
    ruler.add_patterns(patterns)
    ruler.to_disk("Backend\\AudioProcessing\\trained_algorithms\\entity_ruler_activity")

def activity_identifier(text):
    nlp = spacy.load("en_core_web_sm") #load pretrained nlp model
    ruler = nlp.add_pipe("entity_ruler", after="ner") #create entity ruler
    ruler.from_disk("Backend\\AudioProcessing\\trained_algorithms\\entity_ruler_activity") #load entity ruler

    doc = nlp(text) #process the text
    activities_found = []

    for ent in doc.ents: 
        #print (ent.text, ent.label_, ent.ent_id_) #delete later
        if ent.label_ == "ACTIVITY": #check it is a symptom
            print(ent.text)
            acitivity = activity_pattern_processing(ent)
            if acitivity != "Error" and acitivity not in activities_found:
                    activities_found.append(acitivity)               
    return activities_found

def activity_pattern_processing(ent):
    possible_verbs = helpers.load_data("Backend\\AudioProcessing\\trainingData\\activity_verbs.json")
    if ent.ent_id_ == "general_activity":
        for word in ent:
            if word.pos_ == "VERB" and word.lemma_ in possible_verbs:
                #if word.tag_ == "VBG":
                indexOfSpace = ent.text.index(' ')
                if indexOfSpace == -1: 
                    return word.lemma_
                return word.lemma_ + ent.text[(indexOfSpace):] 
                #return ent.text
        return "Error"
    else:
        return ent.ent_id_

def test_activity_func(num1, num2):
    for i in range(num1,num2):
        text = helpers.audio_tests(i)
        print(text)
        print("LIST OF ACTIVITIES", activity_identifier(text))

def test_activity_func_2():
    test_array = ["Last week I went to spain, I partied a lot, I did a barbacue the other day. I had fun with my friends, I drank alcohol and I think that is all. I also caught a plane to come back to the netherlands"]
    for text in test_array:
        print(text)
        print("LIST OF ACTIVITIES", activity_identifier(text))

test_activity_func_2()
# save_entity_ruler_activity()