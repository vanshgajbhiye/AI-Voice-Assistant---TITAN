from core.voice import speak
from core.listener import listen
from core.brain import process_command


speak("kaise hoo app  vansh ")

running = True

while running:

    text = listen()

    if text:

        running = process_command(text)