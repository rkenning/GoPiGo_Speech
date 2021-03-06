#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import string
from pprint import pprint
import re

import Dex_Controller as Dex
import Led_Control as Led
import APIKeys

with open('acc.json','r') as data_file:
	d = data_file.read()
	


#Not implimented the background speech yet but will
def callback(recognizer, audio):
	# received audio data, now we'll recognize it using Google Speech Recognition
	try:
		# for testing purposes, we're just using the default API key
		# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
		# instead of `r.recognize_google(audio)`
		print("Google Speech Recognition thinks you said " + recognizer.recognize_google(audio))
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))



# recognize speech using Microsoft Bing Voice Recognition



if __name__ == '__main__':     # Program start from here
	Led.setup()
	
	try:
		while True:
			
			try:
				Led.spinning()
				r = sr.Recognizer()
				

				with sr.Microphone(device_index =0,
					sample_rate = 44100,
					chunk_size = 512) as source:
					#r.adjust_for_ambient_noise(sr);
					print("Say something!")
					audio = r.listen(source,5,10)
			


				Result = ''
				wordList = ''
				mystr =''
				
				Result = r.recognize_bing(audio, key=BING_KEY)
				Result = Result.upper()
			except sr.UnknownValueError:
				Result = "UNKNOWN"
			except sr.RequestError as e:
				Result = "ERROR"

			print(Result)

			mystr = Result
			wordList = re.sub("[^\w]", " ",  mystr).split()

			for item in wordList:
				Led.LED_Dir(item)
				Dex.Dir(item)
		
			r = ''

	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		Led.destroy()
