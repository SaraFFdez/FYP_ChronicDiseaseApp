import os
import sys
import nltk
import spacy

#Input: a file/text containing the audio in the file
#Output: Depending on the outputs, but multiple arrays/files containing the information we need
def trials(input_text):
    nlp = spacy.blank("en") #creates a blank space for spacy.
    doc = nlp(input_text)
    #text = nltk.tokenize.word_tokenize(input_text)
    #tokenised_text = nltk.pos_tag(text)
    #print(tokenised_text)


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
