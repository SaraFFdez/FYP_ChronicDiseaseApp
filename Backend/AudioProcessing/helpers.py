import json

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

def audio_tests(num):
    test_text_Sukhi = "So today I woke up with a really intense headache where I just had really bad sensitivity to light and I just really felt like I was physically too fatigued to move. So I stayed in bed for about and extra hour today and an hour more than usual. So that brings my total sleep from eight to 9 hours. So roughly about 9 hours of sleep. Other symptoms include I've noticed my allergies a little bit today, so it just kind of stuff. He knows, maybe feeling a little bit ill, but that could just be from my allergies. So I'm not too sure in regards to meals, I just had some eggs in the morning, I had a smoothie and I drank water and I've just now recently had a coffee and for dinner or I'm going to have some chicken. In regards to activities, so I just sort of walked around my bike to work today, which is really good. So that's about five kilometres and I didn't think I'd be able to do that given how tired it was when I woke up and I don't think I have the energy to bike home, so I'm just going to walk to the train station and home. So Yeah."
    test_text_description = "It felt like I had a chronic case of the flu: exhaustion so great I could not move; headaches, dizziness, muscle aches, especially in my legs; and profound exhaustion and mental fogginess, so I could not function. I was sensitive to noise and light. I was amazed that I was so sick physically and yet doctors didn't know what to do."
    rawaan1 = "I woke up very tired today even though I slept for about 8 hours. I woke up with a stuffed nose so I had to use my nasal spray to help me breathe comfortably before leaving home. I took the bus today as I felt tired to walk. I was sleepy throughout the day. In the morning I drank my morning tea with a chocolate cupcake. Then for lunch I had chickenbriani. I ordered take out from Taco Bell for dinner as I was too tired to Cook anything."
    Rhys1 = "Hello test test test test hello app today was not too bad day. I had a pain in my elbow and a sore throat in the morning and that got better into the afternoon. But my knee then started to hurt which caused a pain in my foot while walking. I got tired from all of this and got a headache later into the evening and I'm going to bed. I struggle to sleep after some painful sex and let's hope tomorrow is better."
    negationTry1 = "I did not have a headache today. I did have nausea and some bloating"
    limitTesting = "I had a headache but I did not have any vomiting today."
    negationTry2 = "I have nausea and this morning I had trouble sleeping and my ears hurt"
    rawaan2 = "Woke up very tired today, even though I slept for about 8 hours. I stayed in bed for about an hour before I realised that I would be late for work. I also had a tough nose so I had to use my natural A spray to help me breathe comfortably before leaving home. I walked today as I couldn't catch the bus to work. I was walking slowly today so the commute took me longer than usual. I was sleepy throughout the day, even though I drank my morning tea. I had the tea with the chocolate cupcake. Then for lunch I had chicken Brianne. I didn't eat a proper meal for dinner since I wasn't that hungry and I only made an avocado smoothie with San honey as a sweeter."
    array = [test_text_Sukhi, test_text_description, rawaan1, Rhys1, rawaan2, negationTry1, negationTry2, limitTesting]

    return array[num]