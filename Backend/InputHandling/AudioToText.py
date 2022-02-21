from cgitb import enable
import os
from os import path
import sys
import time

import speech_recognition as sr
from google.cloud import speech
import requests

#----------------------------------------------------------Google Cloud API--------------------------------------------------------
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

#----------------------------------------------------------AssemblyAI--------------------------------------------------------
#helper AssemblyAI
def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data

#helper AssemblyAI
def retrieve_transcript(transcript_id, headers1):
    response = requests.get("https://api.assemblyai.com/v2/transcript/" + transcript_id, headers = headers1)
    return response.json()

def AIspeechToTex(audio):
    #define audio file and API
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), audio)
    API_KEY = '546a6f9de8804c269d59cdcb9056cfa2'

    #upload audio data to their web
    headers = {'authorization': API_KEY}
    audio_url = requests.post('https://api.assemblyai.com/v2/upload',
                        headers=headers,
                        data=read_file(AUDIO_FILE))
    #print(audio_url.json()['upload_url'])

    #send it to the queue to be transcribed
    endpoint = "https://api.assemblyai.com/v2/transcript"
    json = {
        "audio_url": audio_url.json()['upload_url'],
        "language_code": "en_uk"
    }
    headers = {
        "authorization": API_KEY,
        "content-type": "application/json"
    }
    response = requests.post(endpoint, json=json, headers=headers)
    transcript_id = response.json()['id']
    #print(transcript_id)
    
    # Step 2. Retrieve Job Status
    #retrieve until status is completed and print the transciption. Sleep to not make too amany requests (might not be necessary)
    while True:
        time.sleep(3)
        response_status = retrieve_transcript(transcript_id, headers)
        if response_status['status'] == 'completed' :
            print(response_status['text'])
            break  

#---------------------------------------------------------- Sphinx --------------------------------------------------------   
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



