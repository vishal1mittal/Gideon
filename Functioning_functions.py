from Import_Modules import *

def isConnected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        sock = socket.create_connection(("www.google.com", 80))
        if sock is not None:
            print('Clossing socket')
            sock.close
        return True
    except OSError:
        pass
    return False

def talk(messege):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)
    engine.setProperty("rate", 190)
    engine.say(messege)
    engine.runAndWait()

