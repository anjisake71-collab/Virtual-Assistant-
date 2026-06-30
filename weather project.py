'''
import requests

API_KEY = "725a46a93c790aacef366bdab3d97acc"


def get_weather(city):
    
    API_KEY = "725a46a93c790aacef366bdab3d97acc"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:

        response = requests.get(url)

        data = response.json()

        if data["cod"] != 200:
            speak("City not found")
            return

        temperature = data["main"]["temp"]

        humidity = data["main"]["humidity"]

        weather = data["weather"][0]["description"]

        wind = data["wind"]["speed"]

        message = (
            f"Weather in {city}. "
            f"Temperature is {temperature} degree Celsius. "
            f"Humidity is {humidity} percent. "
            f"Weather is {weather}. "
            f"Wind speed is {wind} meters per second."
        )

        speak(message)

    except:
        speak("Unable to fetch weather.")

elif "weather" in command:

    speak("Which city?")

    city = take_command()

    if city != "":
        get_weather(city)

        '''
'''
import requests

# Replace with your OpenWeatherMap API Key
API_KEY = "YOUR_API_KEY"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if str(data["cod"]) != "200":
            speak("Sorry, I could not find that city.")
            return

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        message = (
            f"The weather in {city} is {weather}. "
            f"The temperature is {temperature} degrees Celsius. "
            f"The humidity is {humidity} percent. "
            f"The wind speed is {wind_speed} meters per second."
        )

        speak(message)

    except Exception as e:
        print("Error:", e)
        speak("Sorry, I am unable to fetch the weather information.")

    if "time" in command:
        tell_me()
    elif "weather" in command:
        speak("Which city?")

    city = take_command()

    if city != "":
        get_weather(city)
    else:
        speak("I didn't hear the city name.")       '''

import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import webbrowser
import os
import pyjokes
import requests

# -------------------------------
# TEXT TO SPEECH ENGINE
# -------------------------------
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


# -------------------------------
# TAKE VOICE INPUT
# -------------------------------
def take_command():
    listener = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source, duration=1)
            voice = listener.listen(source)

        command = listener.recognize_google(voice)
        command = command.lower()
        print("User:", command)
        return command

    except:
        return ""


# -------------------------------
# WEATHER FUNCTION
# -------------------------------
API_KEY = "725a46a93c790aacef366bdab3d97acc"


def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if str(data["cod"]) != "200":
            speak("Sorry, I could not find that city.")
            return

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        speak(
            f"The weather in {city} is {weather}. "
            f"The temperature is {temperature} degrees Celsius. "
            f"The humidity is {humidity} percent. "
            f"The wind speed is {wind_speed} meters per second."
        )

    except Exception as e:
        print("Error:", e)
        speak("Sorry, I am unable to fetch the weather information.")


# -------------------------------
# GREETING
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
# MAIN ASSISTANT LOOP
# -------------------------------
def run_assistant():

    greet()

    while True:

        command = take_command()

        if command == "":
            continue

        # TIME
        elif "time" in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time}")

        # DATE
        elif "date" in command:
            date = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Today is {date}")

        # YOUTUBE
        elif "youtube" in command:
            webbrowser.open("https://youtube.com")
            speak("Open YouTube")

        # GOOGLE
        elif "google" in command:
            webbrowser.open("https://google.com")
            speak("Open Google")

        # SEARCH
        elif "search" in command:
            query = command.replace("search", "")
            pywhatkit.search(query)

        # PLAY SONG
        elif "play" in command:
            song = command.replace("play", "")
            pywhatkit.playonyt(song)

        # WIKIPEDIA
        elif "who is" in command:
            person = command.replace("who is", "")
            try:
                info = wikipedia.summary(person, sentences=2)
                speak(info)
            except:
                speak("Sorry, I couldn't find information.")

        # WEATHER
        elif "weather" in command:
            speak("Which city?")
            city = take_command()

            if city != "":
                get_weather(city)
            else:
                speak("I didn't hear the city name.")

        # CALCULATOR (simple)
        elif "calculate" in command:
            expression = command.replace("calculate", "")
            try:
                result = eval(expression)
                speak(f"The answer is {result}")
            except:
                speak("Invalid calculation")

        # OPEN NOTEPAD
        elif "open notepad" in command:
            os.system("notepad")

        # OPEN CALCULATOR
        elif "open calculator" in command:
            os.system("calc")

        # JOKE
        elif "joke" in command:
            joke = pyjokes.get_joke()
            speak(joke)

        # EXIT
        elif "exit" in command or "stop" in command:
            speak("Goodbye")
            break

        else:
            speak("Sorry, I didn't understand that.")


# -------------------------------
# START PROGRAM
# -------------------------------
if __name__ == "__main__":
    run_assistant()