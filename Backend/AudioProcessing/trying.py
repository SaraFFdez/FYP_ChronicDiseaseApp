import spacy
import json
def load_data(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return (data)



text = "allergies"
#symptoms_data = load_data("Backend\\AudioProcessing\\trainingData\\symptoms_data.json")
# print(symptoms_data)
# for item in symptoms_data:
#     text = text + " " + item

nlp = spacy.load("en_core_web_sm")

doc = nlp(text)
for token in doc:
    print (token.text, token.lemma_)