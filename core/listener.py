import speech_recognition as sr

listener = sr.Recognizer()

def listen():

    try:
        with sr.Microphone() as source:

            print("Listening...")

            listener.adjust_for_ambient_noise(source)

            voice = listener.listen(source)

            command = listener.recognize_google(voice)

            command = command.lower()

            print(command)

            return command

    except Exception as e:

        print(e)

        return ""