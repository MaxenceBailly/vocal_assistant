#!/usr/local/bin/python3.8
from os.path import commonpath
import platform
from time import sleep
import os
import yaml

if platform.system() == 'Windows':
    import pyttsx3

#config management
with open("config.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

def talk(text):
    if platform.system() == 'Windows':
        engine = pyttsx3.init()
        for voice in engine.getProperty('voices'):
            if cfg["text_to_speech"]["local"] in voice.name:
                engine.setProperty('voice', voice.id)

        voices = engine.getProperty('voices')
        newVoiceRate = cfg["text_to_speech"]["rate"]
        engine.setProperty('rate', newVoiceRate)
        engine.say(text)
        engine.runAndWait()
    else:
        yml_lang = cfg["text_to_speech"]["local"]
        lang = (yml_lang[0] + yml_lang[1]).lower()

        command = '/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols ' + f"\"http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl={lang}&q=i {text}\""
        os.system(command)

if __name__ == "__main__":
    talk('Bonjour tout le monde')
