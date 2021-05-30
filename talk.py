#!/usr/local/bin/python3.8
from os.path import commonpath
import platform
from time import sleep
import os
import pyttsx3

def talk(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    newVoiceRate = 130
    engine.setProperty('rate', newVoiceRate)
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    talk('Bonjour tout le monde')
