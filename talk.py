import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
newVoiceRate = 130
engine.setProperty('rate',newVoiceRate)

def talk(text):
    """talk function

    Args:
        text (string): text to say
    """
    print(f"--> {text}")
    engine.say(text)
    engine.runAndWait()