import pyttsx3


def speak(text):
    print("GrameenAI:", text)

    engine = pyttsx3.init()   # 🔥 Create fresh engine every time

    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    engine.say(text)
    engine.runAndWait()
    engine.stop()   # 🔥 Important
