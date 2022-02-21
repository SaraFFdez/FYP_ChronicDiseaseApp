import os
import sys
import InputHandling.AudioToText as InpAudio
import AudioProcessing.mainProcessing as ProcMain
def main():
    audioToProcess = "Script1 (faster).wav"
    InpAudio.audioToText(audioToProcess)
    audioToProcess2 = "Script1 (slower).wav"
    InpAudio.audioToText(audioToProcess2)
    audioToProcess3 = "Script1.wav"
    InpAudio.audioToText(audioToProcess3)
    audioToProcess4 = "Script1EngAccent.wav"
    InpAudio.audioToText(audioToProcess4)
    audioToProcess5 = "Script1SpanishAccent.wav"
    InpAudio.audioToText(audioToProcess5)
    ProcMain.textProcessing("Lets go!")

if __name__ == "__main__":
    main()