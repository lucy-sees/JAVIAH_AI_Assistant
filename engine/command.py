import pyttsx3
import speech_recognition as sr
import os
import eel
import time
import random
import datetime
import wikipedia
import webbrowser
import pyautogui
import operator
import requests
import pywhatkit as kit


def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 180)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Lucy!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Lucy!")
    else:
        speak("Good Evening Lucy!")

    speak("Let's get to work. What can I do for you ?")





def takecommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
       
    except Exception as e:
        return ""
    
    return query.lower()


@eel.expose
def allCommands(message=1, start_of_conversation=True):
    if start_of_conversation:
        wishMe()

    while True:
        if message == 1:
            query = takecommand()
            print(query)
            eel.senderText(query)
        else:
            query = message
            eel.senderText(query)

        if query is None:
            print("No command recognized. Please try again.")
            speak("No command recognized. Please try again.")
            continue

        if "exit" in query:
            speak("Goodbye Lucy")
            break
        try:
            if "open" in query:
                from engine.features import openCommand
                openCommand(query)
                speak("Opened" + query)
            #youtube    
            elif "on youtube" in query:
                from engine.features import PlayYoutube
                PlayYoutube(query)

            elif 'open youtube' in query:
                speak("what you will like to watch ?")
                query = takecommand().lower()
                kit.playonyt(f"{query}")

            # who are you
            elif "who are you" in query:
                print("I am Javiah, your virtual assistant")
                speak("I am Javiah, your virtual assistant")
                print(
                    "I am here to help you with your tasks. I can do everything my creator has programmed me to do")
                speak(
                    "I am here to help you with your tasks. I can do everything my creator has programmed me to do")
                
            # who created you
            elif "who created you" in query:
                print(
                    "I don't know who created me, but I was programmed by a tech nerd using Python programming language.")
                speak(
                    "I don't know who created me, but I was programmed by a tech nerd using Python programming language.")

            # wikipedia
            elif 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            # chrome
            elif "open chrome" in query:
                os.system("start chrome")
                speak("Chrome has been opened")
            elif "close chrome" in query:
                os.system("taskkill /f /im chrome.exe")
                speak("Chrome has been closed")

            # microsoft edge
            elif "open microsoft edge" in query:
                os.system("start msedge.exe")
                speak("Microsoft Edge has been opened")
            elif "close microsoft edge" in query:
                os.system("taskkill /f /im msedge.exe")
                speak("Microsoft Edge has been closed")

            # google
            elif "open google" in query:
                speak("What should I search?")
                query = takecommand().lower()
                webbrowser.open(f"https://www.google.com/search?q={query}")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia", results)
            elif "close google" in query:
                os.system("taskkill /f /im msedge.exe")
                speak("Google has been closed")

            # play music
            elif "play music" in query:
                music_dir = "C:\\Users\\BEST\\Music\\all_about_jesus.mp3"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, random.choice(songs)))
            # time
            elif "the time" in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Hey Lucy, the time is {strTime}")

            # stackoverflow
            elif "open stackoverflow" in query:
                speak("Opening Stackoverflow")
                webbrowser.open("stackoverflow.com")
            elif "close stackoverflow" in query:
                os.system("taskkill /f /im msedge.exe")
                speak("Stackoverflow has been closed")

            # whatsapp
            elif "open whatsapp" in query:
                speak("Opening Whatsapp")
                webbrowser.open("https://web.whatsapp.com/")
            elif "close whatsapp" in query:
                os.system("taskkill /f /im msedge.exe")
                speak("Whatsapp has been closed")

            # email
            elif "open email" in query:
                speak("Opening Email")
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            elif "close email" in query:
                os.system("taskkill /f /im msedge.exe")
                speak("Email has been closed")

            # take screenshot
            elif "screenshot" in query:
                speak("What do I name the file?")
                name = takecommand().lower()
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("Screenshot has been taken and saved")
            
             # ip address
            elif "What is my ip address" in query:
                speak("Checking your IP address")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    speak(f"Your IP address is {ipAdd}")
                except Exception as e:
                    speak("Unable to fetch your IP address")
                    print(e)
   
            # calculate
            elif "calculate" in query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("What do you want me to calculate?")
                    print("Listening...")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                    query = r.recognize_google(audio)
                    print(f"User said: {query}")
                    speak(f"The answer is {eval(query)}")
                def get_operator_fn(op):
                    return {
                        '+': operator.add,
                        '-': operator.sub,
                        'x': operator.mul,
                        'divided': operator.__truediv__,
                        'Mod': operator.mod,
                        '^': operator.xor,
                    }[op]
                
                def eval_binary_expr(op1, oper, op2):
                    op1, op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                speak("Your result is")
                speak(eval_binary_expr(*(query.split())))
            
            # volume up  
            elif "volume up" in query:
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                speak("Volume has been increased")
            # volume down
            elif "volume down" in query:
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                speak("Volume has been decreased")
            # mute
            elif "mute" in query:
                pyautogui.press("volumemute")
                speak("Volume has been muted")
            
            # refresh
            elif "refresh" in query:
                pyautogui.moveTo(1551, 551, 2)
                pyautogui.click(x=1551, y=551, clicks=1,
                                interval=0, button='right')
                pyautogui.moveTo(1620, 667, 1)
                pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')
                speak("Page has been refreshed")

            #scroll up
            elif "scroll up" in query:
                pyautogui.scroll(-1000)
                speak("Scrolled up")

            # scroll down
            elif "scroll down" in query:
                pyautogui.scroll(1000)
                speak("Scrolled down")
            
            # open paint
            elif "open paint" in query:
                os.system("start mspaint")
                speak("Paint has been opened")
            
            # draw rectangular spiral
            elif "draw rectangular spiral" in query:
                speak("Drawing rectangular spiral")
                pyautogui.hotkey('win')
                time.sleep(1)
                pyautogui.write('paint')
                time.sleep(1)
                pyautogui.press('enter')
                pyautogui.moveTo(100, 193, 1)
                pyautogui.rightClick
                pyautogui.click()
                distance = 300
                while distance > 0:
                    pyautogui.dragRel(distance, 0, 0.1, button="left")
                    distance = distance - 10
                    pyautogui.dragRel(0, distance, 0.1, button="left")
                    pyautogui.dragRel(-distance, 0, 0.1, button="left")
                    distance = distance - 10
                    pyautogui.dragRel(0, -distance, 0.1, button="left")

            # close paint
            elif "close paint" in query:
                os.system("taskkill /f /im mspaint.exe")
                speak("Paint has been closed")

            # send message and make phonecall
            elif "send message" in query or "phone call" in query or "video call" in query:
                from engine.features import findContact, whatsApp
                flag = ""
                contact_no, name = findContact(query)
                if (contact_no != 0):

                    if "send message" in query:
                        flag = 'message'
                        speak("what message to send")
                        query = takecommand()

                    elif "phone call" in query:
                        flag = 'call'
                    else:
                        flag = 'video call'

                    whatsApp(contact_no, query, flag, name)
            else:
                from engine.features import chatBot
                chatBot(query)
        
            message = 1
        except:
            print("I am sorry, I am not able to process your command")
            speak("I am sorry, I am not able to process your command")
            print("Say that again please...")
            speak("Say that again please...")
            continue

eel.ShowHood()
