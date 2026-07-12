import pyttsx3
import speech_recognition as sr
import mtranslate

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 175)


def speak(audio):
    audio = mtranslate.translate(audio, to_language="en" , from_language="en-in")
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def command():
    content = " "
    while content == " ":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            audio = r.listen(source)
        try:
            print("recognizing...")
            content = r.recognize_google(audio, language='en-in')
            print(f"user said: {content}\n")
        except Exception as e:
            print(e)
            print("say that again please...")
            return "content"
def main_proccess():
    while True:
        request = command()
        if "wake up" in request:
            speak("yess boss! it's  me  your  assistant.How  can  i help  you?")
        else:
            speak("i  am  still  sleeping")

main_proccess()