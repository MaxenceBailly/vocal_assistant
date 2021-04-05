import platform
from time import sleep
import os

if platform.system() == 'Windows':
    import pyttsx3
else:
    from gtts import gTTS
    from playsound import playsound
    # import pyglet

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
        tts = gTTS(text=text, lang='en')
        filename = '/tmp/temp.mp3'
        tts.save(filename)

        playsound(filename)
        # music = pyglet.media.load(filename, streaming=False)
        # music.play()

        # sleep(music.duration) #prevent from killing
        os.remove(filename) #remove temperory file

talk("hello")