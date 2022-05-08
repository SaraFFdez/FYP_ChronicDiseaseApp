import json
import re

def load_data(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return (data)

def save_data(file, data):
    with open (file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def create_training_data(data, type): #could delete later, was used to create entity ruler data. 
    patterns = []
    for item in data:
        pattern = {
            "label": type,
            "pattern": item 
            #"id": item   
        }
        patterns.append(pattern)
    return patterns

#function to find the span of the words in the array_of_symptoms that below to the text
def getting_data(text, array_of_symptoms):
    for symptom in array_of_symptoms:
        match = re.search(symptom, text)
        print (symptom, match)

def audio_tests(num):
    test_text_Sukhi = "So today I woke up with a really intense headache where I just had really bad sensitivity to light and I just really felt like I was physically too fatigued to move. So I stayed in bed for about and extra hour today and an hour more than usual. So that brings my total sleep from eight to 9 hours. So roughly about 9 hours of sleep. Other symptoms include I've noticed my allergies a little bit today, so it just kind of stuff. He knows, maybe feeling a little bit ill, but that could just be from my allergies. So I'm not too sure in regards to meals, I just had some eggs in the morning, I had a smoothie and I drank water and I've just now recently had a coffee and for dinner or I'm going to have some chicken. In regards to activities, so I just sort of walked around my bike to work today, which is really good. So that's about five kilometres and I didn't think I'd be able to do that given how tired it was when I woke up and I don't think I have the energy to bike home, so I'm just going to walk to the train station and home. So Yeah."
    test_text_description = "It felt like I had a chronic case of the flu: exhaustion so great I could not move; headaches, dizziness, muscle aches, especially in my legs; and profound exhaustion and mental fogginess, so I could not function. I was sensitive to noise and light. I was amazed that I was so sick physically and yet doctors didn't know what to do."
    rawaan1 = "I woke up very tired today even though I slept for about 8 hours. I woke up with a stuffed nose so I had to use my nasal spray to help me breathe comfortably before leaving home. I took the bus today as I felt tired to walk. I was sleepy throughout the day. In the morning I drank my morning tea with a chocolate cupcake. Then for lunch I had chickenbriani. I ordered take out from Taco Bell for dinner as I was too tired to Cook anything."
    Rhys1 = "Hello test test test test hello app today was not too bad day. I had a pain in my elbow and a sore throat in the morning and that got better into the afternoon. But my knee then started to hurt which caused a pain in my foot while walking. I got tired from all of this and got a headache later into the evening and I'm going to bed. I struggle to sleep after some painful sex and let's hope tomorrow is better."
    negationTry1 = "I did not have a headache today. I did have nausea and some bloating"
    limitTesting = "I had a headache but I did not have any vomiting today."
    negationTry2 = "I have nausea and this morning I had trouble sleeping and my ears hurt"
    rawaan2 = "Woke up very tired today, even though I slept for about 8 hours. I stayed in bed for about an hour before I realised that I would be late for work. I also had a tough nose so I had to use my natural A spray to help me breathe comfortably before leaving home. I walked today as I couldn't catch the bus to work. I was walking slowly today so the commute took me longer than usual. I was sleepy throughout the day, even though I drank my morning tea. I had the tea with the chocolate cupcake. Then for lunch I had chicken Brianne. I didn't eat a proper meal for dinner since I wasn't that hungry and I only made an avocado smoothie with San honey as a sweeter."
    foodTest1 = "Today I had a banana for breakfast. I had an apple and a pasta plate for lunch. For dinner I am going to eat chicken and rice."
    foodTest2 = "In the morning I had two toasts and an apple. Then I had pasta and coffee for lunch. In the evening I am planning on eating some spaguetti."
    foodTest3 = "Today I ate a banana, a toast and a pizza"
    dani_activity = ["I've gone to the mountain to see the sunset. I have gone to the gym once to do chest. I've watched a movie with friends yesterday night, we had a dinner event that we did. We also went to the engineering ball and had some cocktails there. Had some nice conversations and I would say that are the main things of the week. Also I studied FYP. "]
    rhys_activity = ["On monday I went to the library with Sara. I did some studying and some past papers. On tuesday I went to the library with carmen and in teh evening I watched a football game. I then went back to a friends house to watch a tv show, watched some football and then but some facemasks on the evening. On thrusday I had some final revision prep on the library for my exam and then went home and relaxed. On friday I did my exam and then went climbing in the afternoon. In the evening I went to the cinemas to watch a film. In the Saturday I stayed at home and had a rest most of the day other than to go out on the evening to watch some football."]
    alvaro_activity = ["Last week I went to spain, I partied a lot, I did a barbacue the other day. I had fun with my friends, I drank alcohol and I think that is all. I also caught a plane to come back to the netherlands"]
    kav_activity = ["On monday and tuesday I revised for an exam I had on wednesday then I did more revision for an exam on friday. After my exam on Friday I cycled home and I watched TV and had a nap"]

    array = [test_text_Sukhi, test_text_description, rawaan1, Rhys1, rawaan2, negationTry1, negationTry2, limitTesting]
    food_test = [foodTest1, foodTest2, foodTest3]
    return array[num]