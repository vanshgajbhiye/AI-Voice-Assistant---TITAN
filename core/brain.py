from core.voice import speak
import webbrowser
import os
import pywhatkit
import pyautogui
import time
import wikipedia

def process_command(text):

    text = text.lower()

    print(text)

    # ---------------- YOUTUBE SONG ----------------

    if "play" in text:

        song = text.replace("play", "").strip()

        speak(f"{song} play kar rahi hu")

        pywhatkit.playonyt(song + "song")

    # ---------------- WHATSAPP MESSAGE ----------------

    elif "message" in text:

        speak("Kisko message bhejna hai")

        contact = input("Contact Name: ").lower()

        speak("Kya message bhejna hai")

        msg = input("Message: ")

        # Number yaha manually add karo
        contacts = {
            "mummy" : "+918446937468",
            "papa" : "+918793957719",
            "sujal bhau" : "+919021969427"
        }

        if contact in contacts:
            number = contacts[contact]
     

        pywhatkit.sendwhatmsg_instantly(number, msg)

        speak("Message send kar diya")

    # ---------------- GOOGLE SEARCH ----------------

    elif "search" in text:

        search = text.replace("search", "")

        speak(f"{search} search kar rahi hu")

        pywhatkit.search(search)

    # ---------------- OPEN YOUTUBE ----------------

    elif "youtube" in text:

        speak("YouTube khol rahi hu")

        webbrowser.open("https://youtube.com")

    # ---------------- OPEN GOOGLE ----------------

    elif "google" in text:

        speak("Google khol rahi hu")

        webbrowser.open("https://google.com")

    # ---------------- OPEN CHROME ----------------

    elif "chrome" in text:

        speak("Chrome open kar rahi hu")

        os.system("start chrome")

    # ---------------- WIKIPEDIA ----------------

    elif "who is" in text:

        person = text.replace("who is", "")

        info = wikipedia.summary(person, 2)

        speak(info)

    # ---------------- HELLO ----------------

    elif "hello" in text:

        speak("Hello Vansh")

    # ---------------- NAME ----------------

    elif "tumhara naam" in text:

        speak("Mera naam Tara hai")

    # ---------------- EXIT ----------------

    elif "bye" in text:

        speak("Goodbye Vansh")

        return False

    else:

        speak("Command samaj nahi aayi")

    return True




