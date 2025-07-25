import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime 
import os
import pyautogui
import random
import webbrowser
from plyer import notification
from pygame import mixer
import speedtest


 

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

for i in range(3):
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("e:/python/Jarvis/password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME  Faadi!")
        speak("WELCOME     Fadi!")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")
        speak("Try Again")  

# from INTRO import play_gif
# play_gif              

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding...")
        query = r.recognize_google(audio,language="en-in")
        print(f"You Said: {query}\n")
    except Exception  as e:
        print("Say That Again...")
        return "None"
    return query 

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")
 
if __name__=="__main__":
     while True:
         query = takeCommand().lower()
         if"wake up" in query:
             from GreetMe import greetMe
             greetMe()

             while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok Fadi , You can  call me anytime")
                    break 

                ################# New Functions ################
                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("e:/python/Jarvis/password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done")
                    speak(f"Your new password is{new_pw}")
                
                elif "schedule my day" in query:
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks ( YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("e:/python/Jarvis/tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("e:/python/Jarvis/tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()  
                elif "show my schedule" in query:
                    file = open("e:/python/Jarvis/tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("e:/python/Jarvis/NotificationTone.mp3")
                    mixer.music.play()
                    notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                    )

                elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                    if (a==1):
                        speak("Entering the focus mode....")
                        os.startfile("E:\python\Jarvis\FocusMode.py")
                        exit()
                    else:
                        pass  

                elif "show my focus" in query:
                    from FocusGraph import focus_graph
                    focus_graph()  

                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    translategl(query)

                elif "open" in query:  
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter") 

                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576        
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}") 

                elif "psl score" in query:
                    from plyer import notification  
                    import requests 
                    from bs4 import BeautifulSoup 
                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text,"html.parser")
                    team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                    team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                    a = print(f"{team1} : {team1_score}")
                    b = print(f"{team2} : {team2_score}")

                    notification.notify(
                        title = "PSL SCORE :- ",
                        message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                        timeout = 15
                    )

                elif "play a game" in query:
                    from game import game_play
                    game_play() 

                elif "screenshot" in query:
                    import pyautogui 
                    im = pyautogui.screenshot()
                    im.save("ss.jpg") 

                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")           

                ###################################################
                elif "hello jarvis" in query:
                    speak("Hello Fadi, how are you ?")
                elif "i am fine" in query:
                    speak("that's great,how may i help you Fadi")
                elif "how are you" in query:
                    speak("i am good,how may i help you Fadi")
                elif "thank you" in query:
                    speak("it's my pleasure Fadi")

                elif (query == "play some music" or query == "tried"):
                        speak("Playing your favourite music")
                        a = (1,2,3,4,5,6) 
                        b = random.choice(a)
                        if b== 1:
                            webbrowser.open("https://www.youtube.com/watch?v=3OC_9yQkKjs") 
                        elif b == 2:
                            webbrowser.open("https://www.youtube.com/watch?v=WPLS94_3-JA") 
                        elif b == 3:
                            webbrowser.open("https://www.youtube.com/watch?v=IRBqWn-o-rM")
                        elif b == 4:
                            webbrowser.open("https://www.youtube.com/watch?v=DkAsRwPJnik&list=RD3OC_9yQkKjs&index=3&pp=8AUB") 
                        elif b == 5:
                            webbrowser.open("https://youtu.be/JuXuakMtsMQ?list=RD3OC_9yQkKjs")
                        elif b == 6:
                            webbrowser.open("https://youtu.be/WPLS94_3-JA?list=RD3OC_9yQkKjs")           


                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                    
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down")
                    volumedown()    

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)    

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query) 

                elif "news" in query:
                  from NewsRead import latestnews
                  latestnews()  

                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)

                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()    

                elif "temperature" in query:
                    search = "temperature in mansehra"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "Weather in mansehra"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}") 


                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done  Fadi")    
                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}") 

                elif  (query == "Byee Jarvis" or query == "bhai jarvis"):
                    speak("Good Bye  Fadi, call me any time...")
                    exit()          

                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to "+rememberMessage)
                    remember = open("e:/python/Jarvis/Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("e:/python/Jarvis/Remember.txt","r")
                    speak("You told me to " + remember.read())
                    
                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                if shutdown == "yes":
                    os.system("shutdown /s /t 1")

                elif shutdown == "no": 
                    break
                        
                        