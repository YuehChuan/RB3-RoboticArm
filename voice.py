import speech_recognition as sr 
from difflib import get_close_matches 
import threading


sample_rate = 48000
 
chunk_size = 2048
#Initialize the recognizer 
r = sr.Recognizer() 

mic = sr.Microphone() 

color_pattern = ['blue', 'green', 'yellow', 'red']
action_pattern = ['pickup', 'drop', 'dance']
obj_pattern = ['cube', 'square', 'cuboid', 'rectangle', 'triangle', 'prism', 'cone', 'hexagon', 'circle', 'sphere', 'ball' ]

def closeMatches(patterns, word):
	data = word.split()
	for temp in data: 
		match_list = get_close_matches(temp, patterns)
		if len(match_list) != 0:
			return match_list[0]
	return 1

def detect():
	with mic as source: 
		#wait for a second to let the recognizer adjust the 
		#energy threshold based on the surrounding noise level 
		r.adjust_for_ambient_noise(source) 
		print("Say Something")
		#listens for the user's input 
		audio = r.listen(source) 
			
		try: 
			text = r.recognize_google(audio) 
			print("you said: " + text)
			return text 
		
		#error occurs when google could not understand what was said 
		
		except sr.UnknownValueError: 
			print("Google Speech Recognition could not understand audio")
			return 1 
		
		except sr.RequestError as e: 
			print("Could not request results from Google Speech Recognition service; {0}".format(e))
			return -1


def not_understood():
	print("Sorry, didn't understand that!")

def run():
	while True:
		if (detect() == "dummy"):
			print("what do you want?")
			instruction = detect()
			if (instruction != 1 or instruction != -1):
				action = closeMatches(action_pattern, instruction)
				if action != 1:
					print("Action: " + action)
				else:
					not_understood()
				color = closeMatches(color_pattern, instruction)
				if color != 1:
					print("Color: " + color)
				else:
					not_understood()
				obj = closeMatches(obj_pattern, instruction)
				if obj != 1:
					print("Object: " + obj)
				else:
					not_understood()
			else:
				not_understood()
		else:
			not_understood()

run()