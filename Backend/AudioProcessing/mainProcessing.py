import os
import sys
import nltk
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

#Input: a file/text containing the audio in the file
#Output: Depending on the outputs, but multiple arrays/files containing the information we need
def trials(input_text):
    nlp=spacy.load('en_core_web_sm')
    #nlp = spacy.blank("en") #creates a blank space for spacy.
    doc = nlp(input_text)
    #text = nltk.tokenize.word_tokenize(input_text)
    #tokenised_text = nltk.pos_tag(text)
    #print(tokenised_text)

def getting_data(text, array_of_symptoms):
    for symptom in array_of_symptoms:
        match = re.search(symptom, text)
        print (symptom, match)

text = "People with ME/CFS often describe this experience as a “crash,” “relapse,” or “collapse.” During PEM, any ME/CFS symptoms may get worse or first appear, including difficulty thinking, problems sleeping, sore throat, headaches, feeling dizzy, or severe tiredness. It may take days, weeks, or longer to recover from a crash."
getting_data(text, ["PEM", "loss of energy", "problems sleeping", "difficulty thinking", "headaches", "sore throat", "dizzy", "tiredness"])

def textProcessing(text):
    print("We will process our text here! " + text)


def symptomsList(text):
    print("We will get the syntoms list from the " + text)
    return 

def dietRecord(text):
    print("We will get the table for the diet from the " + text)
    return 

def activityLog(text):
    print("We will get the table for the diet from the " + text)
    return 

def sleepQandQ(text):
    print("We will get the table for the diet from the " + text)
    return 

#helper functions 
