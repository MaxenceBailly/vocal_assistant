#!/usr/local/bin/python3.8
import platform
from time import sleep
import os

if platform.system() == 'Windows':
    import pyttsx3

def talk(text):
    """talk function

    Args:
        text (string): text to say
    """
    if platform.system() == 'Windows':
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[1].id)
        newVoiceRate = 130
        engine.setProperty('rate',newVoiceRate)
        engine.say(text)
        engine.runAndWait()
    else:
        command = os.path.abspath(os.getcwd()) + "/speech.sh " + text
        os.system(command)

if __name__ == "__main__":
    talk("hello")
