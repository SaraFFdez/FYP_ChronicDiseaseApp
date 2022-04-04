import os
import sys
import random
import json
import spacy
import re
from spacy.tokens import DocBin
from tqdm import tqdm

def load_data(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return (data)

def save_data(file, data):
    with open (file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def getting_data(text, array_of_symptoms):
    for symptom in array_of_symptoms:
        match = re.search(symptom, text)
        print (symptom, match)

def change_data_to_v3(TRAIN_DATA):
    nlp = spacy.blank("en") # load a new spacy model
    db = DocBin() # create a DocBin object

    for text, annot in tqdm(TRAIN_DATA): # data in previous format
        doc = nlp.make_doc(text) # create doc object from text
        ents = []
        for start, end, label in annot["entities"]: # add character indexes
            span = doc.char_span(start, end, label=label, alignment_mode="contract")
            if span is None:
                print("Skipping entity")
            else:
                ents.append(span)
        doc.ents = ents # label the text with the ents
        db.add(doc)
    return db

def save_spacy_format():
    TRAIN_DATA = load_data("Backend\\AudioProcessing\\trainingData\\symptomsML_training.json")
    #VALIDATION_DATA = load_data("Backend\\AudioProcessing\\trainingData\\symptomsML_validation.json")
    symptoms_train = change_data_to_v3(TRAIN_DATA)
    #symptoms_validate = change_data_to_v3(VALIDATION_DATA)
    symptoms_train.to_disk("Backend\\AudioProcessing\\trainingData\\symptomsML_training.spacy")
    #symptoms_validate.to_disk("Backend\\AudioProcessing\\trainingData\\symptomsML_validate.spacy")

#IN ORDER TO TRAIN THE DATA RUN THIS IN CLI
# py -m spacy train Backend\\AudioProcessing\\trainingData\\config_SympNER.cfg --output Backend\\AudioProcessing\\trainingData\\symp_NER_model --paths.train Backend\\AudioProcessing\\trainingData\\symptomsML_training.spacy --paths.dev Backend\\AudioProcessing\\trainingData\\symptomsML_validate.spacy

#Test your model
def test_model(text):
    nlp = spacy.load(R"Backend\\AudioProcessing\\trainingData\\symp_NER_model\\model-best")
    doc = nlp(text)
    for ents in doc.ents:
        print(ents.text, ents.label_)

text = "It felt like I had a chronic case of the flu: exhaustion so great I could not move; headaches, dizziness, muscle aches, especially in my legs; and profound exhaustion and mental fogginess, so I could not function. I was sensitive to noise and light. I was amazed that I was so sick physically and yet doctors didn't know what to do."
getting_data(text, ["exhaustion", "headaches", "dizziness", "muscle aches", "exhaustion", "mental fogginess", "sick physically"])

#test_model(text)
# text = "The next day I woke up with the worst sore throat and felt sick overall, but I just kept going, thinking I would get better the next day. I developed bad vertigo, and also had fatigue and sleep problems. I went to the school health clinic and had a lot of tests done. All my tests came back fine— only months later I was found to have mononucleosis."
# getting_data(text, ["sore throat", "sick", "vertigo", "fatigue", "sleep problems"])