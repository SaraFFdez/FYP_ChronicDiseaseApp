import os
import sys
import InputHandling.audioToText as InpAudio
import AudioProcessing.mainProcessing as ProcMain
def main():
    InpAudio.audioToText("First steps here we come")
    ProcMain.textProcessing("Lets go!")

if __name__ == "__main__":
    main()