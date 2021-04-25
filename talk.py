#!/usr/local/bin/python3.8
import platform
from time import sleep
import os

if platform.system() == 'Windows':
    import pyttsx3
else :
    import RPi.GPIO as GPIO
    jaune = int(17)
    verte = int(18)
    bleue = int(27)
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(verte, GPIO.OUT)
    GPIO.setup(jaune, GPIO.OUT)
    GPIO.setup(bleue, GPIO.OUT)

def talk(text):
    """talk function

    Args:
        text (string): text to say
    """
    if platform.system() == 'Windows':
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[0].id)
        newVoiceRate = 130
        engine.setProperty('rate', newVoiceRate)
        engine.say(text)
        engine.runAndWait()
    else:
        command = os.path.abspath(os.getcwd()) + "/speech.sh " + text
        GPIO.output(bleue, GPIO.HIGH)
        os.system(command)
        GPIO.output(bleue, GPIO.LOW)

if __name__ == "__main__":
    talk("Bonjour tout le monde")
