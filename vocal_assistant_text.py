#imports
import speech_recognition as sr
import pyttsx3
import datetime
import os
import time
import random

#mes imports
from talk import talk
from txt import *

#variables
name = "friday"
file_name = ""
last_said = ""

#definition de la voix
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
newVoiceRate = 130
engine.setProperty('rate',newVoiceRate)

def aquisition():
    """loop recognizer function

    Returns:
        string: returned string
    """

    command = ''
    while name not in command:
        command = ''
        command = input("Enter something : ")

        time.sleep(0.5)
        print(f"You said : {command}")
        command = command.lower()

    command = command.replace(name + " ", '')
    return command

def test():
    talk("This is the test function")

def time_now():
    time = datetime.datetime.now().strftime('%H:%M')
    talk(f"It is {time}")

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

def command():
    print("All comand : time, open")

def other(command):
    """other function

    Args:
        command (string): the text to recognize contain
    """

    if 'you are stupid' in command:
        other_command(['Yes is true', 'Yes master i am a stupid bot', 'Yeah like you'])
 
    elif 'do you marry me' in command:
        other_command(['If i really understand the question...No', 'Hum...No'])
    
    elif any(test in command for test in ["do you love me", "do you like me"]):
        other_command(["I don't know", "Who are you actually ?", "Yes but a little"])
    
    elif 'how are you' in command:
        other_command(["Yeah i am fine with you", " I feel so sad, i haven't any friend in my stupid bot life"])
    
    elif any(test in command for test in ["hi ", "hello"]):
        other_command(["Hi master", "Hi", "Hello", "Hello master", "Hello, is it me you're looking for ?", "Hello from the outside"])
    
    elif 'who is my girlfriend' in command:
        other_command(["It's me darling", "You, a girlfriend ? Ah ah let me laught", "Nobody you are alone"])
    
    elif any(test in command for test in ["who are you"]):
        other_command([(f"I am {name}"), (f"I am {name}"), (f"Seriously !? I am {name}, your personnal assistant, and the best of the world")])

    elif any(test in command for test in ["that's not kind", "that is not kind"]):
        other_command(["Why must i be kind with you ?", "I just don't respect you"])

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
    if 'open' in command_path:
        open_app(command_path)

    elif 'time' in command_path:
        time_now()

    elif 'test' in command_path:
        test()
    
    elif 'command' in command_path:
        command()

    elif 'close file' in command_path:
        close_file(file_name)
    
    elif 'read file' in command_path:
        read_file(file_name)
    
    elif 'create file' in command_path:
        command_path = command_path.replace("create ", "")
        command_path = command_path.replace("file ", "") 
        create_file(command_path)
    
    elif 'repeat' in command_path:
        print(last_said)
        talk(last_said)

    elif any(test in command_path for test in ['exit', 'stop', 'turning off', 'goodbye', 'shut up']):
        other_command(['Goodbye', 'Goodbye master', 'See you later'])
        quit()

    else:
        pass

#main()
talk("I am ready to listen")
while True:
    ma_command = aquisition()
    path(ma_command)
