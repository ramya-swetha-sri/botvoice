import datetime
from datetime import date

import mtranslate
import pyttsx3
import speech_recognition as sr

try:
    import pyaudio  # noqa: F401
except ImportError:  # pragma: no cover - runtime dependency guard
    pyaudio = None

engine = pyttsx3.init()
voices = engine.getProperty('voices')
if voices:
    engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 175)


def speak(audio):
    audio = mtranslate.translate(audio, to_language="en" , from_language="en-in")
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def command():
    if pyaudio is None:
        print("PyAudio is not installed. Please install it before using speech input.")
        return ""

    content = " "
    while content == " ":
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("listening...")
                audio = r.listen(source)
        except OSError as exc:
            print(f"Microphone error: {exc}")
            return ""
        try:
            print("recognizing...")
            content = r.recognize_google(audio, language='en-in')
            print(f"user said: {content}\n")
        except Exception as e:
            print(e)
            print("say that again please...")
            return ""
    return content
        

def time():
    print('Hello! Its time!', datetime.now())


def main_proccess():
    while True:
        request = command()
        if not request:
            continue
        if "wake up" in request:
            speak("yess boss! it's  me  your  assistant.How  can  i help  you?")
        elif "sleep" in request:
            speak("i  am  still  sleeping")
        elif "what's the time" in request:
            now_time = datetime.datetime.now().strftime("%H %M")
            speak("Current time is " + str(now_time))
        elif "what's the date" in request:
            today = date.today()
            speak("Today's date is " + str(today))


if __name__ == "__main__":
    main_proccess()