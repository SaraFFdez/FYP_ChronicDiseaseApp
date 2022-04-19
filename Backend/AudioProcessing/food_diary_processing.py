import spacy
import helpers
import json
import numpy as np

def test_food_ML(num1, num2):
    #nlpFood = spacy.load("Backend\\AudioProcessing\\trained_algorithms\\ML\\food_NER_ML\\model-best")
    for i in range(num1,num2):
        text = helpers.audio_tests(i)
        print(text)
        food = food_timing_identificator(text)
        print(food)

def food_timing_identificator(text):
    nlpFood = spacy.load("Backend\\AudioProcessing\\trained_algorithms\\ML\\food_NER_ML\\model-best")
    nlpFood.add_pipe("sentencizer")
    doc = nlpFood(text)
    food_dict = {"no_time" : [], "morning" : [], "afternoon" : [], "evening": []}
    no_food_ents = True
    for ent in doc.ents:
        if ent.label_ == "FOOD":
            #ADD checks here
            print(ent)
            no_food_ents = False
            key = time_of_food(ent.sent.text)
            food_dict[key].append(ent.text)

    if no_food_ents: 
        return dict() #IF NO FOOD ENTITIES FOUND, SEND AN EMPTY DICTIONARY

    return food_dict
     
#takes in a sentence with a food entity, identifies what time of the day it was eaten in. 
def time_of_food(sentence, model_dir = 'Backend\\AudioProcessing\\trained_algorithms\\ML\\food_time_classif_model'):
    threshold = 0.65
    nlpClassify = spacy.load(model_dir) #load model
    doc = nlpClassify(sentence) #process sentence
    max_confidence_label = list(doc.cats.keys())[np.argmax(np.array(list(doc.cats.values())))] #find label

    if doc.cats[max_confidence_label] < threshold: #if it didnt classify it correctly, no time might have been specified
        return "no_time"
    
    if max_confidence_label == "MORNING":
        return "morning"
    elif max_confidence_label == "AFTERNOON":
        return "afternoon"
    elif max_confidence_label == "EVENING":
        return "evening"

    return "no_time"

test_food_ML(0,6)