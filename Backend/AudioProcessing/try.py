from traceback import print_tb
import spacy

nlp = spacy.load("en_core_web_sm")

while True: 
    text = input("input: ")
    doc = nlp(text)
    for token in doc: 
        print (token.text, token.pos_, token.lemma_, token.tag_, token.dep_)
# texts_array = ["I went to the park", "I bought an apple", "I did the paperwork", "I cleaned the house, combed my hair and brushed my teeth"]
# for text in texts_array:
#     doc = nlp(text)
#     for token in doc: 
#         print (token.text, token.pos_, token.lemma_, token.tag_, token.dep_)