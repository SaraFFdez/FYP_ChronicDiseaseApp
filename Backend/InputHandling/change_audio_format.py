import os
# from pydub import AudioSegment

def find_audio(audios):
    files = os.listdir("Backend\\InputHandling")
    for file in files:
        if file.endswith(".wav") or file.endswith(".ogg") or file.endswith(".m4a"):
            if file not in audios:
                return file
    return "Error"
# # files                                                                         
# src = "transcript.mp3"
# dst = "test.wav"

# # convert wav to mp3                                                            
# sound = AudioSegment.from_mp3(src)
# sound.export(dst, format="wav")