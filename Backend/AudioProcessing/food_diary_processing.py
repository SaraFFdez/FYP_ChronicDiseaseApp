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

test_food_ML(0,6)