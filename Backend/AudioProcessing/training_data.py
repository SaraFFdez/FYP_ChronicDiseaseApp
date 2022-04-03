import os
import sys
import random
import json
import spacy
import re

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

def train_spacy(data, iterations):
    TRAIN_DATA = data
    nlp = spacy.blank("en")
    #create ner object
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner, last=True)
    
    for _, annotations in TRAIN_DATA:
        for ent in annotations.get('entities'):
            ner.add_label(ent[2])

    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']

    with nlp.disable_pipes(*other_pipes):  # only train NER
        optimizer = nlp.begin_training()
        for itn in range(iterations):
            print("Statring iteration " + str(itn))
            random.shuffle(TRAIN_DATA)
            losses = {}
            for text, annotations in TRAIN_DATA:
                nlp.update(
                    [text],  # batch of texts
                    [annotations],  # batch of annotations
                    drop=0.2,  # dropout - make it harder to memorise data
                    sgd=optimizer,  # callable to update weights
                    losses=losses)
            print(losses)
    return nlp

TRAIN_DATA = load_data("Backend\\AudioProcessing\\trainingData\\symptomsML_training.json")
prdnlp = train_spacy(TRAIN_DATA, 30)

# Save our trained Model
modelfile = input("symptoms_model")
prdnlp.to_disk(modelfile)

#Test your text
#text = "People with ME/CFS often describe this experience as a “crash,” “relapse,” or “collapse.” During PEM, any ME/CFS symptoms may get worse or first appear, including #difficulty thinking, problems sleeping, sore throat, headaches, feeling dizzy, or severe tiredness. It may take days, weeks, or longer to recover from a crash. Sometimes #patients may be house-bound or even completely bed-bound during crashes. People with ME/CFS may not be able to predict what will cause a crash or how long it will last. "
#test_text = input(text)
#doc = prdnlp(test_text)
#for ent in doc.ents:
#    print(ent.text, ent.start_char, ent.end_char, ent.label_)
#text = "People with ME/CFS often describe this experience as a “crash,” “relapse,” or “collapse.” During PEM, any ME/CFS symptoms may get worse or first appear, including difficulty thinking, problems sleeping, sore throat, headaches, feeling dizzy, or severe tiredness. It may take days, weeks, or longer to recover from a crash."
#getting_data(text, ["PEM", "loss of energy", "problems sleeping", "difficulty thinking", "headaches", "sore throat", "dizzy", "tiredness"])