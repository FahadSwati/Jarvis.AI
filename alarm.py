import pyttsx3
import datetime
import os 

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

extractedtime = open("e:/python/Jarvis/Alarmtext.txt","rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("e:/python/Jarvis/Alarmtext.txt","r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("jarvis","")
    timenow = timenow.replace("set an alarm","")
    timenow = timenow.replace(" and ",":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            speak(" Fadi  Alarm is ringing,")
            os.startfile("e:/python/Jarvis/AlarmTone.mp3") 
        elif currenttime + "00:00:30" == Alarmtime:
            exit()

ring(time)