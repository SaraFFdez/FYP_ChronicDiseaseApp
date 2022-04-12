import os
import sys
import nltk
import json
import spacy
import re

#Input: a file/text containing the audio in the file
#Output: Depending on the outputs, but multiple arrays/files containing the information we need
def trials(input_text):
    symptomsList(input_text)    
    #text = nltk.tokenize.word_tokenize(input_text)
    #tokenised_text = nltk.pos_tag(text)

def textProcessing(text):
    print("We will process our text here! " + text)


def symptomsList(text, model_path = "Backend\\AudioProcessing\\trained_algorithms\\entity_ruler"):
    nlp = spacy.load("en_core_web_sm") #load pretrained nlp model
    ruler = nlp.add_pipe("entity_ruler", after="ner") #create entity ruler
    ruler.from_disk(model_path)
    doc = nlp(text)
    for ent in doc.ents:
        print (ent.text, ent.label_)
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
