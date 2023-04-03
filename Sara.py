from __future__ import print_function
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import time
from time import sleep
import os
from os import startfile
import webbrowser
import keyboard
import selenium
from selenium import webdriver
import wolframalpha
import requests
from threading import Thread

# for google calender api

import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

#google search
import bs4

#openai
import openai

model_engine="text-davinci-003"
# prompt="Hows the weather in New York?"

# for google calender api
SCOPES = ['https://www.googleapis.com/auth/calendar']

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# engine.setProperty('rate',1.7)

#news

again=0

def talk(text):
    engine.say(text)
    engine.runAndWait()

quote_api = "http://api.quotable.io/random"

def random_quote():
    random_quote = requests.get(quote_api).json()
    content = random_quote["content"]
    author = random_quote["author"]
    q=[author, content]
    return q

# A glimpse of all the works Sara can do :

# 1 : open whatsapp and text to any person you want
# 2 : tell you your upcoming meetings, schedules or reminders
# 3 : play a song on spotify
# 4 : play a video on youtube
# 5 : gather the top current news available on internet
# 7 : gather information about something or calculate simple maths calculations
# 7 : search something on internet
# 8 : tell you a beautiful quote every day
# 9 : tell you the current time
# 10 : tells you jokes
# 11 : can open files such as excel, telegram, powerpoint


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
            return command
    except:
        return ''
    # return command

def todaysevents():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        # now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        today = datetime.date.today()
        timeStart = str(today) + "T00:00:00Z"
        timeEnd = str(today) + "T23:59:59Z"
        print("Sir today's schedule include : ")
        talk("Sir today's schedule include : ")
        events_result = service.events().list(calendarId='badalstar1806@gmail.com', timeMin=timeStart, timeMax=timeEnd,
                                              singleEvents=True,
                                              orderBy='startTime', timeZone='Asia/India').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            ind=str(start).index('T')+1
            hour=str(start[ind:ind+2:])
            min=str(start[ind+3:ind+5:])
            last="AM" if int(hour)<=11 else "PM"
            hour=str(abs(int(hour)-12))
            task=str(event['summary'])+" from "+hour+":"+min+" "+last
            print(task)
            talk(task)
            # print(start, event['summary'])

    except HttpError as error:
        print('An error occurred: %s' % error)

# news
def tellmenews():
    india_url="https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey="+news
    india=requests.get(india_url).json()
    india_article=india["articles"]

    apple_url="https://newsapi.org/v2/everything?q=apple&from=2023-04-01&to=2023-04-01&sortBy=popularity&apiKey="+news
    apple=requests.get(apple_url).json()
    apple_article=apple["articles"]

    tesla_url = "https://newsapi.org/v2/everything?q=tesla&from=2023-04-01&to=2023-04-01&sortBy=popularity&apiKey=" + news
    tesla = requests.get(tesla_url).json()
    tesla_article = tesla["articles"]

    news_article = []
    news_article.append("In India,")
    for arti in india_article[:3:]:
        news_article.append(arti['title'])
    news_article.append("In Apple,")
    for arti in apple_article[:3:]:
        news_article.append(arti['title'])
    news_article.append("In Tesla,")
    for arti in tesla_article[:3:]:
        news_article.append(arti['title'])

    for i in range(12):
        print(news_article[i])
        talk(news_article[i])

# greetings
hour,minutes = map(int,str(datetime.datetime.now().strftime('%H:%M')).split(':'))
if hour>=4 and hour<=6:
    talk('Good morning Sir')
    sleep(1)
    talk('You are being very strict to yourself, I appreciate this discipline')
elif hour>6 and (hour<12 and minutes<=59):
    talk('Good morning sir!')
    sleep(1)
    talk('Hope this day brings you a lot of productiveness')
elif hour>=12 and hour<16:
    talk('Good afternoon sir!')
    sleep(1)
else:
    talk('Good evening sir!')
    sleep(1)


def run_sara():

    command = take_command()
    print(command)

    #whatsapp
    if 'send' in command and 'to' not in command:
        talk("Please specify whom to send")
    elif 'send' in command:
        talk("Sending Whatsapp Message...")
        print("Sending Whatsapp Message...")
        hour, minutes = map(int, str(datetime.datetime.now().strftime('%H:%M')).split(':'))

        to=command.index("to")+3

        #phone numbers
        phone="+919123368625" #default
        if command[to::]=='parag':
            phone="+919903364246"
        if command[to::]=='mum' or command[to::]=='mumm' or command[to::]=='mom' or command[to::]=='mummy' or command[to::]=='momm':
            phone="+919007585442"
        if command[to::]=='abhi bhaiya':
            phone="+919163588865"
        if command[to::]=='abhishek bhaiya':
            phone="+916394875951"
        if command[to::]=='papa' or command[to::]=='dad':
            phone="+919007966675"
        if command[to::]=='me':
            phone="+919123368625"



        #message
        mssg="Cool" #default
        mssg_start=command.index("send")+5
        mssg_end=command.index("to")-1
        mssg=command[mssg_start:mssg_end:]

        pywhatkit.sendwhatmsg(phone, mssg , hour,minutes+1)

    #today's schedule : google calender
    elif "today's events" in command or "today's schedule" in command:
        todaysevents()

    #news
    elif "tell" in command and "news" in command or "what" in command and "news" in command or "whats" in command or "news" in command or "current news" in command:

        tellmenews()

    # quote
    elif 'good morning' in command or 'good afternoon' in command or 'good evening' in command or 'good night' in command:
        quote=random_quote()
        talk("Here is a quote by "+ quote[0])
        talk(quote[1])

    #love
    elif 'i love you sara' in command:
        talk('I love you Baadaal')

    # play or pause the song
    elif 'pause' == command or command == 'pause the song' or 'stop'==command or 'stop the song'==command:
        print('pause')
        keyboard.press_and_release('space')
    elif 'play' == command or command == 'pause the song':
        print('play')
        keyboard.press_and_release('space')

    #play on youtube
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
        sleep(7)
        keyboard.press_and_release('space')

    #time
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'whose is your date' in command or 'boyfriend' in command or 'husband' in command or 'are you single' in command:
        talk('sorry, I was created as an AI by Baaadaal, I am loyal to my master')

    # make sara rest
    elif 'rest' in command and 'sara' in command:
        talk('Thank you sir!')
        talk('Take Care')
        quit()
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    # open files : excel, powerpoint, telegram, whatsapp
    #excel
    elif 'open excel' in command:
        talk("Opening Excel...")
        startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk")

    #powepoint
    elif 'open powerpoint' in command or 'open ppt' in command:
        talk("Opening PowerPoint...")
        startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk")

    #telegram
    elif 'open telegram' in command or 'open tele' in command:
        talk("Opening Telegram...")
        startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk")



    elif command=="":
        talk("")

    else:
        # print('Please say the command again.')
        # again+=1
        # if again==7:
        #     talk("Sir, I am still listening.")
        #     again=0
        # prompt = "Hows the weather in New York?"

        completion = openai.Completion.create(
            engine="text-davinci-003",
            prompt=command,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        respon = completion.choices[0].text
        print(respon)
        talk(respon)


        # wikipedia : works on who
        if 'who is' in command:
            person = command.replace('who is ', '')
            print(person)
            info = wikipedia.summary(person, 3)

            person = person.replace(' ', '+')
            webbrowser.open_new("https://www.google.com/search?client=firefox-b-d&q=" + person + "&start")
            # print(info)
            # talk(info)

        elif 'what is' in command:
            search = command.replace('what is ', '')
            search = command.replace(' ', '+')
            webbrowser.open_new("https://www.google.com/search?client=firefox-b-d&q=" + search + "&start")
            sleep(7)

        # google search
        elif 'open' in command or 'what' in command or 'show' in command:
            search = command.replace('open ', '')
            search = command.replace(' ', '+')
            url = "'https://google.com/search?q='" + search
            print(url)
            # webbrowser.open_new("https://www.google.com/search?client=firefox-b-d&q=" + search + "&start")
            request_result = requests.get(url)
            soup = bs4.BeautifulSoup(request_result.text, "html.parser")
            print(soup)
            talk(soup)
            sleep(7)

while True:
    for i in range(3):
        run_sara()

