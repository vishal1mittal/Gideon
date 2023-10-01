import speech_recognition as sr
import pyttsx3
import pywhatkit as kt
import random

# Lists of user greetings and web search keywords
user_Greetings = ["hello", "hi", "hey"]
user_web_search = ["search", "find", "look up"]

# System responses
system_Greetings = ["Hello!", "Hi there!", "Greetings!"]
system_web_search = ["Sure, let me search that for you.", "Certainly, searching now."]

# Initialize speech recognition and text-to-speech engines
r2 = sr.Recognizer()

def talk(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

def handle_greetings(recognized_text):
    if any(x in recognized_text for x in user_Greetings):
        talk(random.choice(system_Greetings))

def handle_web_search(recognized_text):
    if any(x in recognized_text for x in user_web_search):
        talk(random.choice(system_web_search))
        talk("What should I search for, sir?")
        with sr.Microphone() as source:
            audio = r2.listen(source)
        search_query = r2.recognize_google(audio).lower()
        kt.search(search_query)
        talk(f"I found results for {search_query}. Would you like me to open a link?")

# Main loop for speech recognition
while True:
    with sr.Microphone() as source:
        print("Listening...")
        audio = r2.listen(source)

    try:
        recognized_text = r2.recognize_google(audio).lower()
        print("You said: " + recognized_text)
        handle_greetings(recognized_text)
        handle_web_search(recognized_text)

    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
