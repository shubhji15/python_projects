import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

MASTER ='Shubham.....'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
#IT's speak function which will be passed.
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
    
#This function wish me according to the time.


def wishMe():
    hour= int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak('Good Morning'+ MASTER)
    elif hour>=12 and hour<=18:
        speak('Good Afternoon'+MASTER)
    else:
        speak('Good Evening'+MASTER)
    
    speak('How may I help you...')
    


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
        
    try:
        print('Recognizing...')
        query = r.recognize_google(audio,)#Language = 'en=in')
        print(f'user said: {query}\n')
        
    
    except Exception as e:
        print("Say that again please")
        query = None
    return query

    
#Main Program Initialization.....    
speak("Initializing Jin......")
wishMe()
query = takeCommand()

if 'wikipedia' in str(query).lower():
    speak('Searching wikipedia....')
    query = query.replace('wikipedia','')
    results =wikipedia.summary(query,sentences =2)
    speak(results)


elif 'open youtube' in query.lower():
    browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    url = "https://www.youtube.com"
    webbrowser.get(browser_path).open(url)

elif 'open google' in query.lower():
    browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    url = "https://www.google.com"
    webbrowser.get(browser_path).open(url)

elif 'movie' in query:
    speak('Which movie, you want to play')
    choice = takeCommand().capitalize()
    movie_dir = 'D:\\subhi system\\movies'
    movie = os.listdir(movie_dir)
    print(movie)
    for i in range(0,len(movie)):
        if ((movie[i].capitalize()).startswith(choice)):
            os.startfile(os.path.join(movie_dir,movie[i]))
            break
    else:
        speak("Movie doesn't exist in the directory" )


elif 'play songs by youtube' in query.lower():
    browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    url = "https://www.youtube.com/watch?v=WvKJln22-3w"
    webbrowser.get(browser_path).open(url)


elif 'the time' in query.lower():
    strTime =datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{MASTER} the time is {strTime}")

else:
    speak("i Don't know")





