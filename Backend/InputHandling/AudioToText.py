from cgitb import enable
import os
from os import path
import sys
import speech_recognition as sr
from google.cloud import speech

def googleCloudspeechToTex(audio):
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), audio)
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'Backend\googleSpeechCloudKey2.json'
    speech_client = speech.SpeechClient()
    with open(AUDIO_FILE, 'rb') as f1:
        byte_data = f1.read()
    pAudio = speech.RecognitionAudio(content = byte_data)

    config = speech.RecognitionConfig( #doesnt need to be a wav file which is nice. 
        sample_rate_hertz = 48000,
        enable_automatic_punctuation=True,
        language_code = 'en-US',
        audio_channel_count=1 #what this?
    )
    #recognize method for small local files (there is another for longer files)
    response_standard_wav = speech_client.recognize(
    config=config,
    audio=pAudio
    )
    print(response_standard_wav)

#Input: an audio file
#Output: a file/text containing the audio in the file
def audioToTextSphinx(audio):
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

    return
#helper functions 



