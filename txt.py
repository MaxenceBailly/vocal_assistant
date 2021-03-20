import pyttsx3
from pathlib import Path
from talk import talk

#definition de la voix
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
newVoiceRate = 130
engine.setProperty('rate',newVoiceRate)

def write_file():
    pass

def readline_file():
    pass

def read_file(name_file):
    print(name_file.read())

def open_file(name_file):
    name_file = name_file.replace(" ", "_")
    if Path(f'C:/Users/maxen/Desktop/txt_file_friday/{name_file}.txt').is_file():
        file = open(f"C:/Users/maxen/Desktop/txt_file_friday/{name_file}.txt", "w")
        talk(f"{name_file} is opened")
    else:
        talk("File not exist")

def create_file(name_file):
    name_file = name_file.replace(" ", "_")
    fullpath = f'C:/Users/maxen/Desktop/txt_file_friday/{name_file}.txt'

    if Path(fullpath).is_file():
        talk("The file already exist")
    else:
        file = open(fullpath, "w")
        file.close()
        name_file = name_file.replace("_", " ")
        talk(f"{name_file} is created")    

def remove_file():
    pass

def close_file(name_file):
    name_file.close()
    talk(f"{name_file} is closed")