'''
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import webbrowser
import os
#initialize voice engine

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
#2.take voice command

def take_command():
    listener = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source)

    try:
        command = listener.recognize_google(voice)
        command = command.lower()
        print(command)
        return command

    except:
        return ""
    
#3.take voice command
hour = datetime.datetime.now().hour

if hour < 12:
    speak("Good Morning")

elif hour < 18:
    speak("Good Afternoon")

else:
    speak("Good Evening")

speak("How can I help you?")

#creating a main function

def run_assistant():
    
    while True:

        command = take_command()

        if "time" in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(time)

        elif "date" in command:
            date = datetime.datetime.now().strftime("%d %B %Y")
            speak(date)

        elif "youtube" in command:
            webbrowser.open("https://youtube.com")

        elif "google" in command:
            webbrowser.open("https://google.com")

        elif "search" in command:
            command = command.replace("search","")
            pywhatkit.search(command)

        elif "play" in command:
            song = command.replace("play","")
            pywhatkit.playonyt(song)

        elif "who is" in command:
            person = command.replace("who is","")
            info = wikipedia.summary(person,2)
            speak(info)

        elif "exit" in command:
            speak("Goodbye")
            break

run_assistant()

print("What is the time?")
print("What is today's date?")
print("Open YouTube")
print("Open Google")
print("Play Shape of You")
print("Who is Albert Einstein?")
print("Search Python tutorial")
print("Exit")

#adding calculator
elif "calculate" in command:
    
    expression = command.replace("calculate","")

    result = eval(expression)

    speak(f"The answer is {result}")

#notepad

elif "open notepad" in command:
    
    os.system("notepad")

#open calculator
elif "open calculator" in command:
    
    os.system("calc")

#open camera

elif "camera" in command:
    
    os.system("start microsoft.windows.camera:")

#adding jokes
import pyjokes

elif "joke" in command:
    joke = pyjokes.get_joke()
    speak(joke)

#weather '''

import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import webbrowser
import os
import pyjokes

# -------------------------------
# Initialize Voice Engine
# -------------------------------
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


# -------------------------------
# Take Voice Command
# -------------------------------
def take_command():
    listener = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source, duration=1)
        voice = listener.listen(source)

    try:
        command = listener.recognize_google(voice)
        command = command.lower()
        print("You:", command)
        return command

    except:
        return ""


# -------------------------------
# Greeting
# -------------------------------
def greet():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning")

    elif hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("How can I help you?")


# -------------------------------
# Main Assistant
# -------------------------------
def run_assistant():

    greet()

    while True:

        command = take_command()

        if command == "":
            continue

        # Time
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}")

        # Date
        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Today is {current_date}")

        # Open YouTube
        elif "youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        # Open Google
        elif "google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        # Search
        elif "search" in command:
            search = command.replace("search", "")
            speak(f"Searching for {search}")
            pywhatkit.search(search)

        # Play Song
        elif "play" in command:
            song = command.replace("play", "")
            speak(f"Playing {song}")
            pywhatkit.playonyt(song)

        # Wikipedia
        elif "who is" in command:
            person = command.replace("who is", "")

            try:
                info = wikipedia.summary(person, sentences=2)
                speak(info)

            except:
                speak("Sorry, I couldn't find information.")

        # Calculator
        elif "calculate" in command:

            expression = command.replace("calculate", "")

            try:
                result = eval(expression)
                speak(f"The answer is {result}")

            except:
                speak("Invalid calculation")

        # Notepad
        elif "open notepad" in command:
            speak("Opening Notepad")
            os.system("notepad")

        # Calculator App
        elif "open calculator" in command:
            speak("Opening Calculator")
            os.system("calc")

        # Camera
        elif "camera" in command:
            speak("Opening Camera")
            os.system("start microsoft.windows.camera:")

        # Joke
        elif "joke" in command:
            joke = pyjokes.get_joke()
            speak(joke)

        # Exit
        elif "exit" in command or "stop" in command:
            speak("Goodbye")
            break

        else:
            speak("Sorry, I didn't understand that command.")


# -------------------------------
# Run Program
# -------------------------------
if __name__ == "__main__":
    run_assistant()

