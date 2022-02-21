import os
from os import path
import sys
import speech_recognition as sr
#import sphinxbase
#import pocketsphinx


#Input: an audio file
#Output: a file/text containing the audio in the file
def audioToText(audio):
    # obtain path to the audio in the same folder as this script!!
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), audio)

    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file

    # recognize speech using Sphinx
    try:
        print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

    # recognize speech using Google Speech Recognition
    #try:
    #    # for testing purposes, we're just using the default API key
    #    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")` instead of `r.recognize_google(audio)`
    #    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    #except sr.UnknownValueError:
    #    print("Google Speech Recognition could not understand audio")
    #except sr.RequestError as e:
    #    print("Could not request results from Google Speech Recognition service; {0}".format(e))
#
    #GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"fypapp-341220-587a36006eab.json"
    #try:
    #    print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
    #except sr.UnknownValueError:
    #    print("Google Cloud Speech Recognition could not understand audio")
    #except sr.RequestError as e:
    #    print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    return

def notes(audio):
    return audioToText(audio)

#helper functions 



