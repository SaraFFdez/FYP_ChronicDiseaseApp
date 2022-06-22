import os
import sys
import InputHandling.AudioToText as InpAudio
import AudioProcessing.mainProcessing as ProcMain
import InputHandling.change_audio_format as getAudio
import time
import pymongo
import datetime

def main():
    
  #tic = time.perf_counter()
  audios = []
  while str(getAudio.find_audio(audios)) != "Error":
    audios.append(str(getAudio.find_audio(audios)))
  #audioToProcess = str(getAudio.find_audio())
  #print(audioToProcess)
  for audioToProcess in audios:
    print(audioToProcess)
    transcript = InpAudio.AIspeechToTex(audioToProcess)
    #transcript = "Today I had avocado toast for breakfast and then coffee and fruit for a snack and chicken for dinner. I skipped lunch. In the morning I went to gym and after that I studied at home and later in the afternoon I went out to play mini golf with friends. When I woke up I was a bit nauseous and busy, but later on I was fine."
    print("Transcript: ", transcript)
    if transcript == "Error":
      print("There was an error")
    else:
      #client = pymongo.MongoClient("mongodb+srv://sf3218:1Jo41mJdyA6XLeDm@cluster0.ayhp3hd.mongodb.net/?retryWrites=true&w=majority")
      #db = client.test
      symptomsList, foodDiary1, foodDiary2, activityList = ProcMain.speech_processing_main(transcript)
      print("SYMPTOM LIST:", symptomsList)
      #print("FOOD DIARY DICTIONARY (FIRST ML):", foodDiary1)
      print("FOOD DIARY DICTIONARY:", foodDiary2)
      print("ACTIVITY LIST:", activityList)
      #data = {"SYMPTOM LIST": symptomsList, "FOOD DIARY DICTIONARY": foodDiary, "ACTIVITY LIST": activityList, "status": "sent"}
      #FYPset = db.FYP
      #results = FYPset.insert_one(data)
      #toc = time.perf_counter()
      #print(f"Time taken: {toc - tic:0.4f} seconds")
    

if __name__ == "__main__":
    main()