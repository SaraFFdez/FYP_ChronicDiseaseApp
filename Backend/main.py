import os
import sys
import InputHandling.audioToText as InpAudio
import AudioProcessing.mainProcessing as ProcMain
def main():
    audioToProcess = "audio_files_harvard.wav"
    InpAudio.audioToText(audioToProcess)
    ProcMain.textProcessing("Lets go!")

if __name__ == "__main__":
    main()