import datetime
from datetime import date

import mtranslate
import pyttsx3
import speech_recognition as sr
import pyautogui

try:
    import pyaudio  # noqa: F401
except ImportError:  # pragma: no cover - runtime dependency guard
    pyaudio = None

engine = pyttsx3.init()
voices = engine.getProperty('voices')

preferred_voice_ids = [
    'com.apple.voice.compact.en-US.Samantha',
    'com.apple.voice.compact.en-GB.Susan',
    'com.apple.voice.compact.en-US.Ava',
    'com.apple.voice.compact.en-IE.Moira',
    'com.apple.voice.compact.en-US.Jane',
    'com.apple.voice.compact.en-US.Emma',
    'com.apple.voice.compact.en-US.Alex',
]

selected_voice_id = None
for voice in voices:
    if voice.id in preferred_voice_ids:
        selected_voice_id = voice.id
        break

if selected_voice_id:
    engine.setProperty('voice', selected_voice_id)
elif voices:
    engine.setProperty('voice', voices[0].id)

engine.setProperty('rate', 175)


def speak(audio):
    try:
        audio = mtranslate.translate(audio, to_language="en", from_language="en-in")
    except Exception as exc:
        print(f"Translation warning: {exc}")

    print(audio)
    try:
        engine.say(audio)
        engine.runAndWait()
    except Exception as exc:
        print(f"Speech error: {exc}")


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
            speak("Message sent")
        elif "open" in request:
            query = request.replace("open", "").strip()
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")
            speak("Opening " + query)
        elif "close" in request:
            pyautogui.hotkey('alt', 'F4')
            speak("Closing")


if __name__ == "__main__":
    main_proccess()