import os
import sys
import InputHandling.AudioToText as InpAudio
import AudioProcessing.mainProcessing as ProcMain
import time

def main():
    #tic = time.perf_counter()
    audioToProcess = "Diary-2-Rawan.wav"
    transcript = InpAudio.AIspeechToTex(audioToProcess)
    print("Transcript: ", transcript)
    if transcript == "Error":
      print("There was an error")
    else:
      symptomsList, foodDiary, activityList = ProcMain.speech_processing_main(transcript)
      print("SYMPTOM LIST:", symptomsList)
      print("FOOD DIARY DICTIONARY:", foodDiary)
      print("ACTIVITY LIST:", activityList)
    
    
    #toc = time.perf_counter()
    #print(f"Time taken: {toc - tic:0.4f} seconds")
    

if __name__ == "__main__":
    main()