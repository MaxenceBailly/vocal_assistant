import pyaudio
import speech_recognition as sr
import time
from talk import talk

listener = sr.Recognizer()

with sr.Microphone() as source:
    listener.adjust_for_ambient_noise(source, duration=0.2)
    listener.energy_threshold = 2000
    print("Listening...", str(listener.energy_threshold))
    try:
        voice = listener.listen(source, timeout=5.0)
        command = listener.recognize_google(voice, language="fr-FR")
    except:
        voice = ""
        command = ""

time.sleep(0.5)
print(f"You said : {command}")