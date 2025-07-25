import requests
import json
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    api_dict = {"business" : "https://gnews.io/api/v4/top-headlines?country=pk&category=business&apikey=e15330cdb399459d93c69d665d3dff22",
            "entertainment" : "https://gnews.io/api/v4/top-headlines?country=pk&category=entertainment&apikey=e15330cdb399459d93c69d665d3dff22",
            "health" : "https://gnews.io/api/v4/top-headlines?country=pk&category=general&apikey=e15330cdb399459d93c69d665d3dff22",
            "science" :"https://newsdata.io/api/1/sources?country=pk&apikey=e15330cdb399459d93c69d665d3dff22",
            "sports" :"https://gnews.io/api/v4/top-headlines?country=pk&category=sports&apikey=e15330cdb399459d93c69d665d3dff22",
            "technology" :"https://gnews.io/api/v4/top-headlines?country=pk&category=technology&apikey=e15330cdb399459d93c69d665d3dff22"}

    content = None
    url = None
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field = input("Type field news that you want: ")
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
        
    speak("thats all")


    


