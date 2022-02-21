import os
import sys
import InputHandling.AudioToText as InpAudio
import AudioProcessing.mainProcessing as ProcMain
import time

def main():
    tic = time.perf_counter()
    audioToProcess = "Script1 (slower).wav"
    InpAudio.AIspeechToTex(audioToProcess)
    toc = time.perf_counter()
    print(f"Time taken: {toc - tic:0.4f} seconds")
    

if __name__ == "__main__":
    main()