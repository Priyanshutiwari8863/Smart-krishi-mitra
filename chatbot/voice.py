import speech_recognition as sr
from gtts import gTTS
import os

def listen_voice():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='hi-IN')
        return text
    except Exception as e:
        return "समझ नहीं आया"

def speak(text):
    tts = gTTS(text, lang='hi')
    tts.save("voice.mp3")
    os.system("start voice.mp3")