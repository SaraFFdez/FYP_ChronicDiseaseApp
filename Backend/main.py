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
  audioToProcess = str(getAudio.find_audio_wav())
  print(audioToProcess)
  transcript = InpAudio.AIspeechToTex(audioToProcess)
  print("Transcript: ", transcript)
  if transcript == "Error":
    print("There was an error")
  else:
    client = pymongo.MongoClient("mongodb+srv://sf3218:1Jo41mJdyA6XLeDm@cluster0.ayhp3hd.mongodb.net/?retryWrites=true&w=majority")
    db = client.test
    symptomsList, foodDiary, activityList = ProcMain.speech_processing_main(transcript)
    print("SYMPTOM LIST:", symptomsList)
    print("FOOD DIARY DICTIONARY:", foodDiary)
    print("ACTIVITY LIST:", activityList)
    data = {"SYMPTOM LIST": symptomsList, "FOOD DIARY DICTIONARY": foodDiary, "ACTIVITY LIST": activityList, "status": "sent"}
    FYPset = db.FYP
    results = FYPset.insert_one(data)
    #toc = time.perf_counter()
    #print(f"Time taken: {toc - tic:0.4f} seconds")
    

if __name__ == "__main__":
    main()