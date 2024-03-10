import pyttsx3
import speech_recognition as sr
import os
import datetime
import wikipedia
import webbrowser
import pywhatkit as wk
import openai
import random
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('Ai')[1:]).strip() }.txt", "w") as f:
        f.write(text)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon ")
    else:
        speak("good evening")
    speak("ready to Comply.What can i do for You")


def takecommand():
     r = sr.Recognizer()
     with sr.Microphone() as source:
         print('listening ..')
         r.pause_threshold = 1
         audio = r.listen(source)

     try:
         print("recognising")
         query = r.recognize_google(audio , language= 'en-in')
         print(f" user said: {query}\n")

     except Exception as e :
         print('say that again ...')
         return "none"
     return query


wishMe()
while True:
    query = takecommand().lower()
    if "ai" in query:
        print("yes sir")
        speak('yes sir')

    elif "who are you" in query:
        print("my name in siomAi")
        speak("my name in siomAi")
        print("I can do everything that my creater programmed me to do ")
        speak("I can do everything that my creater programmed me to do ")

    elif "who created you" in query:
        print('Rishi ,Rishav , subham ', "they have created me ")
        speak('Rishi ,Rishav , subham ', "they have created me ")

    elif 'what is ' in query:
        speak('searching Wikipedia...')
        query = query.replace("what is","")
        results = wikipedia.summary(query,sentence=2)
        speak("according to wikipedia")
        print(results)
        speak(results)

    elif'who is' in query:
        speak('searching Wikipedia...')
        query = query.replace("who is", "")
        results = wikipedia.summary(query, sentence=2)
        speak("according to wikipedia")
        print(results)
        speak(results)

    elif "just open google" in query:
        webbrowser.open('google.com')

    elif 'open google' in query:
        speak("what should i search ?")
        qry = takecommand().lower()
        webbrowser.open(f"{qry}")
        results = wikipedia.summary(qry, sentences = 1)
        speak(results)

    elif 'just open youtube' in query:
        webbrowser.open('youtube.com')


    elif 'open youtube'in query:
        speak('what you will like to watch ?')
        qrry = takecommand().lower()
        wk.playonyt(f"{qrry}")

    elif 'search on youtube'in query:
        query = query.replace("search on youtube", "")
        webbrowser.open(f"www.youtube.com/results?Search_query = {query}")

    elif 'close browser' in query:
        os.system("taskkill/f/im chrome.exe")


    elif 'open notepad' in query:
        npath = "C:\WINDOWS\system32\\notepad.exe"
        os.startfile(npath)

    elif "close notepad" in query:
        os.system("taskkill/f/im notepad.exe")

    elif "open command prompt" in query:
        os.system("start cmd ")

    elif 'close command prompt' in query:
        os.system("taskkill /f/im cmd.exe")

    elif 'what is the time ' in query:
        strTime = datetime.datetime.now().strftime("%H:%m:%s")
        speak(f"Sir the time is {strTime}")

    elif "shut down the system " in query:
        os.system("shutdown /s /t 5")


    elif "restart the system " in query:
        os.system("shutdown /r/t 5 ")

if "Using Ai ".lower() in query.lower():
    ai(prompt=query)
