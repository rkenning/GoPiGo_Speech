#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import json
from pprint import pprint

with open('acc.json','r') as data_file:
    d = data_file.read()


# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone(device_index =0,
	sample_rate = 44100,
	chunk_size = 512) as source:
    print("Say something!")
    audio = r.listen(source)


# recognize speech using Microsoft Bing Voice Recognition
BING_KEY = "3115dd2606fe4be7a043f68d46a13890" # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
try:
    print("Microsoft Bing Voice Recognition thinks you said ---" + r.recognize_bing(audio, key=BING_KEY))
except sr.UnknownValueError:
    print("Microsoft Bing Voice Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

