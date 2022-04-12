import spacy

nlp = spacy.load("en_core_web_sm")
text = "So today I woke up with a really intense headache where I just had really bad sensitivity to light and I just really felt like I was physically too fatigued to move. So I stayed in bed for about and extra hour today and an hour more than usual. So that brings my total sleep from eight to 9 hours. So roughly about 9 hours of sleep. Other symptoms include I've noticed my allergies a little bit today, so it just kind of stuff. He knows, maybe feeling a little bit ill, but that could just be from my allergies. So I'm not too sure in regards to meals, I just had some eggs in the morning, I had a smoothie and I drank water and I've just now recently had a coffee and for dinner or I'm going to have some chicken. In regards to activities, so I just sort of walked around my bike to work today, which is really good. So that's about five kilometres and I didn't think I'd be able to do that given how tired it was when I woke up and I don't think I have the energy to bike home, so I'm just going to walk to the train station and home. So Yeah."

doc1 = nlp(text)
doc2 = nlp("fatigued")
for token in doc2:
    if token.text == "fatigued":
        print(token.text, token.lemma_)
for ents in doc1.ents:
    print(ents.text, ents.ent_id_)