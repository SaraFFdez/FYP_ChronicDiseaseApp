import spacy
import numpy as np

#returns a dictionary of the foods in the text and the time they were consumed at.
def food_timing_identificator(text, model_dir = "Backend\\AudioProcessing\\trained_algorithms\\ML\\food_NER_ML\\model-best"):
    nlpFood = spacy.load(model_dir) #load pretrained model
    nlpFood.add_pipe("sentencizer")
    doc = nlpFood(text) 
    food_dict = {"no_time" : [], "morning" : [], "afternoon" : [], "evening": []} #initialize the dictionary
    no_food_ents = True

    for ent in doc.ents:
        if ent.label_ == "FOOD":
            #do we want any checks like: this thing is a noun (which i am pretty sure it should be lol)?
            no_food_ents = False
            key = time_of_food(ent.sent.text)
            food_dict[key].append(ent.text)

    if no_food_ents: 
        return dict() #if no food entities found, return an empty dictionary

    return food_dict
     
#takes in a sentence with a food entity, identifies what time of the day it was eaten in and returns it. 
def time_of_food(sentence, model_dir = 'Backend\\AudioProcessing\\trained_algorithms\\ML\\food_time_classif_model'):
    threshold = 0.65
    nlpClassify = spacy.load(model_dir) #load classification model
    doc = nlpClassify(sentence) #process sentence
    max_confidence_label = list(doc.cats.keys())[np.argmax(np.array(list(doc.cats.values())))] #find label

    if doc.cats[max_confidence_label] < threshold: #if it is not past a certain threshold, assume no time has been specified
        return "no_time"
    
    #return max_confidence_label.lower()
    if max_confidence_label == "MORNING":
        return "morning"
    elif max_confidence_label == "AFTERNOON":
        return "afternoon"
    elif max_confidence_label == "EVENING":
        return "evening"

    return "no_time"