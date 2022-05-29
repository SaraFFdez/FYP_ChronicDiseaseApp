import spacy
import numpy as np

#returns a dictionary of the foods in the text and the time they were consumed at.
def food_timing_identificator(text, model_dir = "Backend\\AudioProcessing\\trained_algorithms\\ML\\food_NER_ML\\model-best"):
    #nlpFood = spacy.load(model_dir) #load pretrained model
    nlpFood = spacy.load("en_food_ner")
    nlpFood.add_pipe("sentencizer")
    doc = nlpFood(text) 
    food_dict = {"no_time" : [], "morning" : [], "afternoon" : [], "evening": []} #initialize the dictionary
    no_food_ents = True
    foods_no_classif = []

    for ent in doc.ents:
        if ent.label_ == "FOOD":
            no_food_ents = False
            key = time_of_food(ent.sent.text)
            if key == "no_time":
                foods_no_classif.append(ent.text)
            else:
                food_dict[key].append(ent.text)
            
    if len(foods_no_classif) != 0:
        nlp = spacy.load("en_core_web_sm")
        processed_text = preprocessing(text)
        doc2 = nlp(processed_text)
        for food in foods_no_classif:
            for token in doc2:
                if token.text in food:
                   key = time_of_food(token.sent.text)
                   food_dict[key].append(food) 
                   break

    if no_food_ents: 
        return dict() #if no food entities found, return an empty dictionary

    return food_dict

def food_timing_identificator_modif(text, model_dir = "Backend\\AudioProcessing\\trained_algorithms\\ML\\food_NER_ML\\model-best"):
    nlpFood = spacy.load(model_dir) #load pretrained model
    #nlpFood = spacy.load("en_food_ner")
    nlpFood.add_pipe("sentencizer")
    doc = nlpFood(text) 
    food_dict = {"no_time" : [], "morning" : [], "afternoon" : [], "evening": []} #initialize the dictionary
    no_food_ents = True
    foods_no_classif = []

    for ent in doc.ents:
        if ent.label_ == "FOOD":
            no_food_ents = False
            key = time_of_food(ent.sent.text)
            if key == "no_time":
                foods_no_classif.append(ent.text)
            else:
                food_dict[key].append(ent.text)
            
    if len(foods_no_classif) != 0:
        nlp = spacy.load("en_core_web_sm")
        processed_text = preprocessing(text)
        doc2 = nlp(processed_text)
        for food in foods_no_classif:
            for token in doc2:
                if token.text in food:
                   key = time_of_food(token.sent.text)
                   food_dict[key].append(food) 
                   break

    if no_food_ents: 
        return dict() #if no food entities found, return an empty dictionary

    return food_dict
     
#takes in a sentence with a food entity, identifies what time of the day it was eaten in and returns it. 
def time_of_food(sentence, model_dir = 'Backend\\AudioProcessing\\trained_algorithms\\ML\\food_time_classif_model'):
    threshold = 0.65
    nlpClassify = spacy.load(model_dir) #load classification model
    doc = nlpClassify(sentence) #process sentence
    max_confidence_label = list(doc.cats.keys())[np.argmax(np.array(list(doc.cats.values())))] #find label

    if doc.cats[max_confidence_label] < threshold: #if it is not past a certain threshold, assume no time has been specified
        return "no_time"
    
    #return max_confidence_label.lower()
    if max_confidence_label == "MORNING":
        return "morning"
    elif max_confidence_label == "AFTERNOON":
        return "afternoon"
    elif max_confidence_label == "EVENING":
        return "evening"

    return "no_time"

def preprocessing(text):
    text = text.replace(" and ", ". ")
    text = text.replace(", ", ". ")
    return text

def test_food(text_array):
    for text in text_array:
        print(text)
        print(food_timing_identificator(text))
        print(food_timing_identificator_modif(text))


def testTexts():
    t1 = "So today I have eaten for breakfast rice cakes with bananas, for lunch two fish cakes and for dinner meatballs with cauliflower and two toasts. I have taken an hour walk in the park and I've gone to the gym where I did wait for 45 minutes and the symptoms I felt were mainly headaches and back pain."
    t2 = "On Monday I had hamburgers for breakfast, chicken and rice for lunch and avocado toast for snack before dinner which I had a Taco Bell. When I woke up I had a bit of a headache and I felt bit dizzy and also it was really sensitive to light but I did not have any bloating like usual and for activities I did some running in the morning and then went to gym and I've I went back home to study and then I took a bath after that."
    t3 =" Basically, I had burritos for lunch and steak with fries for dinner. For the activities we did the Sprite challenge, which was super cool, consists of drinking two cans of Sprite and trying not to die. It's really difficult. "
    t4 = "Hello. Good evening. App, health, app, whatever, I call you. How are you doing today? Today, for me was a strange day. In the morning, I had a pastel de Nata or an took egg tarts, if you will. That was for breakfast. And it was okay. It made me a bit gassy, a little bloated, but nothing too bad. And then in the afternoon, I went out with some friends to mini golf. And I beat them all because I'm better than at the mini golf. And I had a little bit of Sprite, a little drink of Sprite while I was there. And I felt okay after that, I had a bit of a headache from all the flashing lights. But I was okay. I wasn't too bad. And then into the evening, I just had a nice rest at home. And I didn't feel too bad. I didn't feel too bad. So not a terrible day. And I'll let you know how I feel tomorrow."
    t5 = "Today I ate pizza and I also had Chinese stir Fry. I practised for an exam and prepared a presentation. I also played some games. Other than that, I didn't really feel any symptoms. Don't really feel tired or anything. Not coughing, not sick, nothing like that."
    t6 = "This morning I woke up and I was very hungry. So for breakfast I had scrambled eggs with olive oil and then some bread. And then I also ate a banana. And I had a glass of milk to try to make it as Valance as possible. And then I was in a very good mood. And half morning I felt a bit peckish. So I had a snack. I have heard that nuts are very good for you. So I have some nuts. And then midday, since I had already had some nuts for a snack, I wasn't overly hungry. So I had some sandwich with cheese and tomato. And I also had two Tangerines. I only did like house chores this morning. I felt a bit breathless at times and I coughed a few times, but not many, but it was a coarse cough. Then in the afternoon, since the weather was nice, I thought I would go for a walk. So I walked down the Hill and then I came back. It's a relatively steep Hill, so the whole thing took me about an hour. By the time I got up the Hill, I was tired and I was breathless. But then again, it takes an effort to go up and down the Hill. I had coffee when I arrived home with two biscuits. And I also put some sugar in the coffee. Then I made dinner and I tied up some clothes. So basically I work a little bit around the house. And then for dinner I made a chicken stew. I had two plates of it. It didn't have a lot of chicken. It had quite a lot of vegetables. And then I had a piece of extravague dessert "
    t7 = "This morning I woke up and I ate some Greek yoghurt with grapes. I felt tired and hungry. After this, I ate some cinnamon swirls and I felt less hungry but I had a fever and a sore throat at this time. After this I went to go play badminton. I walked through Hyde Park which was nice but the wind was blowing so I felt cold and I shivered. Then when I got to the sports Hall, I played badminton but I hurt my wrist and I scratched my wrist as well. So I had a scratch and I had a sprained wrist. After this I went to go eat food, but the food was poisoned so I got salmonella and I got a temperature. Then I came back home and I played some video games, but I had eyes trained because the computer screen was too bright and the sun was shining and reflecting off of the screen. So my eyes hurt and I had ache coming from my forehead. Then I went to sleep because I felt really tired."
    return [t1,t2,t3, t4, t5,t6, t7]

test_food(testTexts())

