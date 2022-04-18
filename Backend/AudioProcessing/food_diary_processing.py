import spacy
import helpers
import json

def test_food_ML(num1, num2):
    nlpFood = spacy.load("Backend\\AudioProcessing\\trained_algorithms\\ML\\food_NER_ML\\model-best")
    for i in range(num1,num2):
        text = helpers.audio_tests(i)
        print(text)
        doc = nlpFood(text)
        for ent in doc.ents:
            print (ent, ent.label_)

def food_timing_identificator(text):
    nlpFood = spacy.load("Backend\\AudioProcessing\\trained_algorithms\\ML\\food_NER_ML\\model-best")
    doc = nlpFood(text)
    food_dict = {"no_time" : [], "morning" : [], "afternoon" : [], "evening": []}
    no_food_ents = True
    for ent in doc.ents:
        if ent.label_ == "FOOD":
            #ADD checks here
            no_food_ents = False
            key = time_of_food(ent.sent.text, nlpFood)
            food_dict[key].append(ent.text)

    if no_food_ents: 
        return dict() #IF NO FOOD ENTITIES FOUND, SEND AN EMPTY DICTIONARY

    return food_dict
     
#takes in a sentence with a food entity, identifies what time of the day it was eaten in. 
def time_of_food(sentence,nlp):
    doc = nlp(sentence)
    for token in doc: 
        time = time_identificator(token)
        if time != None:
            return time
    return "no_time"

def time_identificator(token): #This will be expanded
    if token == "morning" or token == "A.M" or token == "AM":
        return "morning"
    elif token == "afternoon" or token == "P.M":
        return "afternoon"
    elif token == "evening":
        return "evening"
    else:
        return None

test_food_ML(0,6)