import webbrowser
import re
import random
import time
from pyowm import OWM
from bs4 import BeautifulSoup as soup
import wikipedia
import smtplib
import ssl
import subprocess
import speech_recognition as sr
import requests
import json
import datetime
import sys
import GoogleScraper
import urllib.parse
import pyttsx3
import email
import pyaudio


# we need to either do the django part for our AI if we our making an app or website, or we can make it like siri
# where the user can talk to instead so we don't have to do the Django Part, but in that case we will need to use It
# works offline which will be advantage for us in the presentation where we can state that someone can get help even
# when they don't have internet connection
# we need to create a speech_recognition function
# Make the medical assistant work fully offline

# speech_recognition part to make it possible we need it to be able to speak more than 2 parameters we need to
# customize the voice and make sure it can talk longer sentences and do it faster
def speak(Hi):
    engine = pyttsx3.init()
    engine.say(Hi)
    hi = engine.runAndWait()

    return hi


def speak2(Hello, World):
    engine = pyttsx3.init()
    engine.say(Hello, World)
    engine.runAndWait()


# This is asking them for their name so they can refer back and add it to the database
Intro = input(speak("Hey there!, I am your new personal assistant. Nice to meet you, for future references may I ask, "
                    "What is your name ?"))
# This will speak Hello and then your name
speak("Hello" + Intro)

while True:

    answer = input(speak("what can I help you with today?")).strip()

    # This checks for keywords in the code, and will do commands according to them
    # This is searching in google
    if "search" in answer:

        new = 2
        tabUrl = "http://google.com?#q="
        term = input(speak("Enter search query: "))
        webbrowser.open(tabUrl + term, new=new)
        speak("Your requested command has been completed")

    else:
        pass

    # Opening websites in google
    if 'open' in answer:
        reg_ex = re.search('open (.+)', answer)
        if reg_ex:
            domain = reg_ex.group(1)
            speak(domain)
            url = 'https://www.' + domain
            webbrowser.open_new_tab(url)
            speak('The website you have requested has been opened for you' + Intro)

        else:
            pass

    # Simple Calculator
    if "calculator" in answer:
        operation = input(speak("Would you like to Multiply, Divide, Subtract or Add?"))
        num1 = int(input(speak("What is your first number?")))
        num2 = int(input(speak("What is your second number?")))

        if "Multiply" in operation:
            print("your answer is", num1 * num2)

        else:
            pass

        if "Divide" in operation:
            print("your answer is", num1 / num2)

        else:
            pass
        if "Subtract" in operation:
            print("your answer is", num1 - num2)

        if "Add" in operation:
            print("your answer is", num1 + num2)

        else:
            pass

    # Flips a coin
    if "coin" in answer:
        Result = random.randint(1, 2)

        if Result == 1:
            speak("You got Heads")
        else:
            speak("You got Tails")

    # Roll's a Dice
    if "dice" in answer:
        number = random.randint(1, 6)
        print("You rolled", number)

    else:
        pass

    # Set timer
    if "timer" in answer:

        seconds = int(speak(input("How many seconds would you like your timer to be?")))
        while seconds != 0:
            seconds = seconds - 1
            time.sleep(1)
            speak(seconds)

    else:
        pass

    # Play Music
    if "music" in answer:

        URL = "https://www.youtube.com/watch?v=SQ1ED8-tBpE"
        webbrowser.open(URL)
        speak("Your Request has been fulfilled")

    else:
        pass

    # Uses API to check for the weather
    if 'current weather' in answer:
        reg_ex = re.search('current weather in (.*)', answer)
        if reg_ex:
            city = reg_ex.group(1)
            owm = OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
            obs = owm.weather_at_place(city)
            w = obs.get_weather()
            k = w.get_status()
            x = w.get_temperature(unit='celsius')
            speak(
                'Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f '
                'degree celsius' % (
                    city, k, x['temp_max'], x['temp_min']))

    else:
        pass

    # Opens google news, if someone wants to read the news
    if 'news' in answer:
        webbrowser.open("https://news.google.com/?taa=1&hl=en-CA&gl=CA&ceid=CA:en")

    else:
        pass

    # If you want to research on wikipedia, it will first give you all the options on the topic and then you can
    # choose one you want to research
    if "wikipedia" in answer:
        wiki = input(speak("what would you like to research in wikipedia?"))
        speak(wikipedia.search(wiki))
        wiki2 = input("which one of those would you like to know about?")
        OGURL = "https://en.wikipedia.org/wiki/"
        webbrowser.open(OGURL + wiki2)

    else:
        pass

    # It can open apps, Needs work and doesn't work
    if 'launch' in answer:
        reg_ex = re.search('launch (.*)', answer)
        if reg_ex:
            appname = reg_ex.group(1)
            appname1 = appname + ".app"
            subprocess.Popen(["open", "-n", "/Applications/" + appname1], stdout=subprocess.PIPE)
        speak('I have launched the desired application')

    else:
        pass

    # Tells the current time
    if 'time' in answer:

        now = datetime.datetime.now()
        speak('Current time is %d hours %d minutes' % (now.hour, now.minute))

    else:
        pass

    # Tells the richest person in the world
    if "richest person" in answer:
        speak("Jeff Bezos is the Richest currently!!!!!!!!")
        url2 = "https://www.forbes.com/billionaires/list/;#version:realtime"
        webbrowser.open(url2)

    else:
        pass

    # Current Cricket scores
    if "cricket scores" in answer:

        url3 = "https://www.cricbuzz.com/"
        webbrowser.open(url3)

    else:
        pass

    # Current NBA scores
    if "nba scores" in answer:
        url4 = "https://nba.com"
        webbrowser.open(url4)

    else:
        pass

    # This is the start to our medical assistant
    # Solutions to the symptoms need more work, and detail.
    # We need to add more solution's to other problems
    if "medical" in answer:

        medical_info = speak("Thank you for reaching out to us for your health problems, ")

        # It will first ask for your phone number, then it will send that to the database so in case someone's
        # condition get's worse the hospital cna look at what they had first and contact them back
        speak("because this data will be sent to hospital we request you type in your phone ")
        input(int(speak("number so we can reach out to you later, in case your health get's worse")))

        speak("Plz list all the problem's you are currently experiencing separated by a ")

        # Asks to list all symptoms you are facing, so it can inform you on what might you have
        medical_problem = input(speak("comma, based on that we  will inform you on what to do"))

        # Checks what symptoms you have and tell's you what to do when you have that
        if "headache" in medical_problem:

            speak("To get relief from your headache you can take medicine such as advil, there are also other drugs ")
            speak("that ")
            speak("you can get in a pharmacy that could be close by too you that can help with a headache")

            url3 = "http://google.com?#q=what+to+do+when+you+have+a+headache"
            webbrowser.open_new_tab(url3)

            speak("I have also opened a website, that can assist you with your headache")

        else:
            pass

        if "fever" in medical_problem:
            speak("To get relief from your fever you can take medicine such as advil, there are also other drugs that "
                  "you can get in a pharmacy that could be close by too you that can help with a fever")

            url3 = "http://google.com?#q=what+to+do+when+you+have+a+fever"
            webbrowser.open_new_tab(url3)

            speak("I have also opened a website, that can assist you with your fever")

        else:
            pass

        if "cough" in medical_problem:
            speak("Persistent a cough could be a symptom of respiratory tract infection that can assist you with "
                  "your fever such as chronic bronchitis or asthama.")
            speak("These diseases have other symptoms such as wheezing, chest tightness and shortness of breath")
            speak(
                "To help with your cough you can take cough syrup, but read the label for side effects of cough syrup")
            speak("If you think your cough is getting worse seek medical assistance as soon as possible")

        else:
            pass

        if "injury" in medical_problem:
            speak("Apply pressure ot the wound and stop the bleeding as soon as possible")
            speak("after clean the wound with anti-septic cloth or just simply water, next bandage it or cover it")
            speak(
                "with something(if you don't have a bandage) so it doesn't get infected, if the problem is too seriuos "
                "seek medical help as soon as possible")

    # Asks if you would like more help or do anything else
    answer2 = input(speak("Would you like to do something else?"))

    if "yes" in answer2:
        continue

    elif "no" in answer2:
        speak("Thank you, come again")
        break

    else:
        speak("Sorry I don't no what you mean")

        # If it did not understand your first answer it will ask again to confirm
        answer3 = input(speak("Would you like to do something else?  print  y  or n"))

        if "y" in answer3:
            continue

        elif "n" in answer3:
            speak("Thank you, Hope you had a great day, plz feel free to come back")
            break
