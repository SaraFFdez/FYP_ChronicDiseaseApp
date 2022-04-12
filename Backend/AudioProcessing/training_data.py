import os
import sys
import random
import json
import spacy
import re
from spacy.tokens import DocBin
from tqdm import tqdm
import helpers

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
    TRAIN_DATA = helpers.load_data("Backend\\AudioProcessing\\trainingData\\symptomsML_training.json")
    data_split_val = 0.3
    VALIDATION_DATA = [] 
    for i in range(0,int(len(TRAIN_DATA)*data_split_val)):
        data = random.choice(TRAIN_DATA)
        VALIDATION_DATA.append(data)
        TRAIN_DATA.remove(data)
    symptoms_train = change_data_to_v3(TRAIN_DATA)
    symptoms_validate = change_data_to_v3(VALIDATION_DATA)
    symptoms_train.to_disk("Backend\\AudioProcessing\\trainingData\\symptomsML_training.spacy")
    symptoms_validate.to_disk("Backend\\AudioProcessing\\trainingData\\symptomsML_validate.spacy")

#IN ORDER TO TRAIN THE DATA RUN THIS IN CLI
# py -m spacy train Backend\\AudioProcessing\\trainingData\\config_SympNER.cfg --output Backend\\AudioProcessing\\trainingData\\symp_NER_model --paths.train Backend\\AudioProcessing\\trainingData\\symptomsML_training.spacy --paths.dev Backend\\AudioProcessing\\trainingData\\symptomsML_validate.spacy
#save_spacy_format()

#Test your model
def test_model(text):
    nlpSymp = spacy.load(R"Backend\\AudioProcessing\\trainingData\\symp_NER_model\\model-best")
    doc = nlpSymp(text)
    for ents in doc.ents:
        print(ents.text, ents.label_)

#test_text = "I have a headache and I was not very tired today, but yesteday I had a toothache and vomited"
test_text_Sukhi = "So today in regards to symptoms I woke up with a headache that seemed to get a little bit better as the day progressed, but I still had headache that I found a little bit debilitating. Definitely woke up extremely tired. Tough time getting out of bed, but it again started getting better throughout the day but still had trouble focusing and trouble concentrating on tasks. Physically I've also felt fairly tired, so it's been quite tough to manoeuvre around and feel motivated to walk around. But yeah, those are the symptoms today in regards to meals, I didn't eat until about 01:00 P.m. Where I had some Curry and rice, I had a coffee in the morning and I've had a decent amount of water today. What I mean decent probably about a litre this far in regards to activities, nothing too intense today I've just walked to the train station. However, I'm going to try to go to the gym today and we will see what the outcome of that is tomorrow. But I'm feeling energised enough to go to the gym today."
#test_text_Sukhi2 = "So today I woke up with a really intense headache where I just had really bad sensitivity to light and I just really felt like I was physically too fatigued to move. So I stayed in bed for about and extra hour today and an hour more than usual. So that brings my total sleep from eight to 9 hours. So roughly about 9 hours of sleep. Other symptoms include I've noticed my allergies a little bit today, so it just kind of stuff. He knows, maybe feeling a little bit ill, but that could just be from my allergies. So I'm not too sure in regards to meals, I just had some eggs in the morning, I had a smoothie and I drank water and I've just now recently had a coffee and for dinner or I'm going to have some chicken. In regards to activities, so I just sort of walked around my bike to work today, which is really good. So that's about five kilometres and I didn't think I'd be able to do that given how tired it was when I woke up and I don't think I have the energy to bike home, so I'm just going to walk to the train station and home. So Yeah."
#test_text = "It felt like I had a chronic case of the flu: exhaustion so great I could not move; headaches, dizziness, muscle aches, especially in my legs; and profound exhaustion and mental fogginess, so I could not function. I was sensitive to noise and light. I was amazed that I was so sick physically and yet doctors didn't know what to do."
test_model(test_text_Sukhi)

#text = "I have a headache and I was not very tired today"
# getting_data(text, ["headache", "tired"])