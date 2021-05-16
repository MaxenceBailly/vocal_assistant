#!/usr/local/bin/python3.8
from os.path import commonpath
import platform
from time import sleep
import os

if platform.system() == 'Windows':
    import pyttsx3

def talk(text):
    if platform.system() == 'Windows':
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        newVoiceRate = 130
        engine.setProperty('rate', newVoiceRate)
        engine.say(text)
        engine.runAndWait()
    else:
        command = '/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols ' + f"\"http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=fr&q=i {text}\""
        #command = os.path.abspath(os.getcwd()) + '/speech.sh ' + text
        os.system(command)

if __name__ == "__main__":
    talk('Bonjour tout le monde')
