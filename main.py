import speech_recognition as sr
import pyttsx3
import asyncio
from ai import ask

r = sr.Recognizer()
engine = pyttsx3.init()

print("Listening...")

async def answer(speech):
    response = await ask(speech).replace("\n", " ") # This calls the AI engine
    print(response + "\n")
    engine.say(response) # Speak the response
    engine.runAndWait()

while True:
    with sr.Microphone() as source: # Grab mic
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            # This converts the speech to text.
            speech = r.recognize_google(audio).lower().replace("hi assist", "hey assist").replace("hello assist", "hey assist")

            if "hey assist" in speech and speech != "":
                speech = speech.replace("hey assist", "")
                print(">>> " + speech)
                asyncio.run(answer(speech))
                engine.say("Hi")

        except sr.UnknownValueError:
            pass # Ignore errors.
