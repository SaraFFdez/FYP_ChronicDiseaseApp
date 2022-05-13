import os
# from pydub import AudioSegment

def find_audio_wav():
    files = os.listdir("Backend\\InputHandling")
    for file in files:
        if file.endswith(".wav"):
            return file

# # files                                                                         
# src = "transcript.mp3"
# dst = "test.wav"

# # convert wav to mp3                                                            
# sound = AudioSegment.from_mp3(src)
# sound.export(dst, format="wav")