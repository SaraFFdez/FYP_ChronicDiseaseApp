from curses import nl
import os
import sys
import json
import spacy
import re
from entity_ruler import symptoms_identifier

#Input: a file/text containing the audio in the file
#Output: Depending on the outputs, but multiple arrays/files containing the information we need
def trials(input_text):
    symptomsList(input_text)    
    #text = nltk.tokenize.word_tokenize(input_text)
    #tokenised_text = nltk.pos_tag(text)

def textProcessing(text):
    print("We will process our text here! " + text) #possibly the " but " to ". "


def symptomsList(text):
    symptoms_identifier(text)

def dietRecord(text):
    nlpFood = spacy.load("Backend\\AudioProcessing\\trained_algorithms\\ML\\food_NER_ML")
    doc = nlpFood(text)
    for ent in doc.ents:
        print (ent, ent.label_)
    return 

def activityLog(text):
    print("We will get the table for the diet from the " + text)
    return 

def sleepQandQ(text):
    print("We will get the table for the diet from the " + text)
    return 

#helper functions 
