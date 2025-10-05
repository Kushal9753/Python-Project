import pyttsx3

print("Welcome to RoboSpeaker 1.1 Created by Kushal")

engine = pyttsx3.init()

while True:
    text = input("Enter what you want me to speak:- ")
    if text.lower() == "exit":
        print("Goodbye!")
        break
    engine.say(text)
    engine.runAndWait()
