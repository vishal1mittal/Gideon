import speech_recognition as sr
import pyttsx3
import socket
from MydataSets import *
from VariablesAndCodes import *
from Functioning_functions import *
import random
import re
import pywhatkit as kt


r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()
running_state = True
while running_state:
    with sr.Microphone() as source:
        print("Listning")
        audio = r3.listen(source)

    recognized_text = r2.recognize_google(audio).lower()
    print(recognized_text)

    if any(x in recognized_text for x in user_Greetings):
        
        talk(random.choice(system_Greetings))

    elif recognized_text == "exit":
        running_state = False


    elif any(x in recognized_text for x in user_web_search):
        talk(random.choice(system_web_search))
        talk("what should i search for sir?")

        with sr.Microphone() as source:
            audio = r1.listen(source)
        kt.search(r1.recognize_google(audio).lower())