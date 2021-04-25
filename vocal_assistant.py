#!/usr/local/bin/python3.8

#imports
import platform
import pyaudio
import speech_recognition as sr
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

import datetime
import os
import time
import random

#mes imports
from talk import *
from txt import *
from remind import *

#variables
va_keyword = "sarah"
file_name = ""

def aquisition():
    """loop recognizer function

    Returns:
        string: returned string
    """

    command = ''
    listener = sr.Recognizer()
    if platform.system() == 'Windows':
        mic = sr.Microphone()
    else:
        mic = sr.Microphone(device_index=microphone_index)

    while va_keyword not in command:
        command = ''
        with mic as source:
            listener.adjust_for_ambient_noise(source , duration=0.2)
            if platform.system() == 'Windows': 
                listener.energy_threshold = 2000

            print("----------\nJ'écoute...") #, str(listener.energy_threshold))
            try:
                if platform.system() != 'Windows':
                    GPIO.output(verte, GPIO.HIGH)
                    GPIO.output(jaune, GPIO.LOW)

                voice = listener.listen(source, timeout=5.0)

                if platform.system() != 'Windows':
                    GPIO.output(verte, GPIO.LOW)
                    GPIO.output(jaune, GPIO.HIGH)
                print("stop")
                command = listener.recognize_google(voice, language="fr-FR")
            except:
                print(f"Vous n'avez rien dit")
            else:
                time.sleep(0.5)
                print(f"Vous avez dit : {command}")
                command = command.lower()

    command = command.replace(va_keyword + " ", '')
    return command

def test():
    talk("C'est une fonction test")

def time_now():
    time = datetime.datetime.now().strftime('%H:%M')
    talk(f"Il est {time}")

def open_app(command_path):
    if 'minecraft launcher' in command_path:
        talk("I open Minecraft Launcher")
        os.startfile("C:/Program Files (x86)/Minecraft Launcher/MinecraftLauncher.exe")
        
    elif "assassin's creed chronicles china" in command_path:
        talk("I open Assassin's Creed chronicles china")
        os.startfile("uplay://launch/1651/0")
    
    elif 'discord' in command_path:
        talk("I open Discord")
        os.startfile("C:/Users/maxen/AppData/Local/Discord/app-0.0.308/Discord.exe")
    
    elif 'ubisoft' in command_path:
        talk("I open Ubsoft Connect")
        os.startfile("C:/Program Files (x86)/Ubisoft/Ubisoft Game Launcher/UbisoftConnect.exe")
    
    elif 'file' in command_path:
        file_name = command_path.replace("friday open file ", "")
        open_file(file_name)

    else:
        talk("I don't understand your open request, repeat please")

def other(command):
    """other function

    Args:
        command (string): the text to recognize contain
    """

    if 'tu es stupide' in command:
        other_command(["Oui c'est vraie", "Oui maître je suis un robot stupide", "Ouais comme toi"])
 
    elif "veux-tu m'épouser" in command:
        other_command(["Si j'ai bien compris la question...Non", 'Hum...Non'])
    
    elif any(test in command for test in ["m'aime tu", "est-ce que tu m'aime"]):
        other_command(["Je sais pas", "Tu es qui déjà ?", "Oui mais juste un peu"])
    
    elif 'comment vas-tu' in command:
        other_command(["Ouai je suis bien avec toi", "Je me sens triste, j'ai aucun ami dans ma stupide vie de robot"])
    
    elif any(test in command for test in ["salut", "bonjour"]):
        other_command(["Bonjour maître", "Salut", "Bonjour"]) #, "Hello, is it me you're looking for ?", "Hello from the outside"])
    
    elif 'qui est ma petite amie' in command:
        other_command(["C'est moi chérie", "Toi, une petite amie ? Ah ah laisse moi rire", "Personne t'es tout seul"])
    
    elif any(test in command for test in ["qui est tu"]):
        other_command([(f"Je suis {va_keyword}"), (f"Je m'appelle {va_keyword}"), (f"Sérieusement !? Je suis {va_keyword}, votre assistant personnel, et le meilleur au monde")])

    elif any(test in command for test in ["c'est pas gentil"]):
        other_command(["Pourquoi je devrais être gentille avec vous ?", "Je ne te respecte pas"])

def other_command(list):
    """function other command wich return a sentence of list

    Args:
        list (list): list of sentence to choice randomly
    """

    len_list = len(list)
    random_number = random.randint(0, (len_list-1))
    talk(list[random_number])

def path(command_path):
    """function path to execute every command

    Args:
        command_path (string): text to analyzing
    """

    if command_path != "":
        other(command_path)
    if 'ouvre' in command_path:
        open_app(command_path)

    elif 'heure' in command_path:
        time_now()

    elif 'test' in command_path:
        test()

    elif 'ferme le fichier' in command_path:
        close_file(file_name)
    
    elif 'lie le fichier' in command_path:
        read_file(file_name)
    
    elif 'crée le fichier' in command_path:
        command_path = command_path.replace("crée le fichier ", "")
        create_file(command_path)
    
    elif 'rappelle' in command_path:
        remind(command_path)

    elif any(test in command_path for test in ['au revoir', 'stop']):
        other_command(['Au revoir', 'Au revoir maître', 'À la prochaine'])
        quit()

    else:
        pass

#main()
if platform.system() == 'Windows':
    print("windows détecté.")
else:
    for index, device_name in enumerate(sr.Microphone.list_microphone_names()):
        print("{0} - {1}".format(index, device_name))
    print(f"Veuillez choisir un microphone : ")
    microphone_index = int(input())

talk("Je suis prête")
while True:
    ma_command = aquisition()
    path(ma_command)
