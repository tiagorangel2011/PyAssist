import speech_recognition as sr
import pyttsx3
import asyncio
from ai import ask

r = sr.Recognizer()
engine = pyttsx3.init()

async def answer(speech):
    response = await ask(speech)
    print(response.replace("\n", " ") + "\n")
    engine.say(response)
    engine.runAndWait()

while True:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            # sometimes the engine thinks clippy means "creepy"
            speech = r.recognize_google(audio).lower().replace("hi clippy", "hey clippy").replace("hello clippy", "hey clippy").replace("creepy", "clippy")

            if "hey clippy" in speech and speech != "":
                speech = speech.replace("hey clippy", "")
                print(">>> " + speech)
                asyncio.run(answer(speech))
                engine.say("Hi")

        except sr.UnknownValueError:
            pass
