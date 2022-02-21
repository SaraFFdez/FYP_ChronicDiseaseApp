import os
import sys
import InputHandling.AudioToText as InpAudio
import AudioProcessing.mainProcessing as ProcMain
def main():
    audioToProcess = "FirstFYPaudio.wav"
    InpAudio.audioToText(audioToProcess)
    ProcMain.textProcessing("Lets go!")

if __name__ == "__main__":
    main()