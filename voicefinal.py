import pyttsx3 
# Module that facilitates the program to convert text into to audio output
import speech_recognition as sr 
# Module helps interpret the user input in the form of a string.
# SpeechRecognition library allows Python to access audio from your system’s microphone, transcribe the audio, and save it.
import datetime 
# Module to access date and time
import wikipedia 
# Module to search in wikipedia and obtain answers
# Wikipedia is used to fetch a variety of information from the Wikipedia website.
import webbrowser 
# Module to open browser based on audio input
# Web browser package provides a high-level interface that allows displaying Web-based pages to users.
import os 
# Module to access various documents present in the Library.
import wolframalpha
# API which can compute expert-level answers using Wolfram's algorithms, knowledgebase and AI technology.
import requests
# Module allows you to send HTTP requests using Python
import time
import json
from urllib.request import urlopen
# urllib is a package of requests to access URLs
from selenium import webdriver
# Module that is used to carry out automated test cases for browsers or web applications.
import pyjokes
import subprocess
import notif
import simulator
from plyer import notification
# A platform-independent api to use features.
from bs4 import BeautifulSoup
# a Python library that makes it used to scrape information from web pages.

print("===========          Initialising Your Desktop Voice Assistant           ===============")
#speak(" Intialising Jarvis...")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):# The function required to give audio output to the Voice Assistant
    engine.say(audio)
    engine.runAndWait()

def wishMe(): # Defining the function that gives appropriate greeting based on the time 
    hour = int(datetime.datetime.now().hour) 
    if  hour>=0 and hour<12:
        speak("Good Morning! Suki")
    elif hour==12 and hour<18:
        speak("Good Afternoon! Suki")    
    else:
        speak("Good Evening! Suki ")
    speak("I am Coco , your desktop voice assistant , How may I help you today? ")
    # Utilising the speak function to display the required output required    

def takeCommand():# It takes microphone input from the user and returns string output
    r= sr.Recognizer()# Defining the function required to interpret the audio input
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
    # Setting the time for the program to wait before executing the task
        audio = r.listen(source) 

    try:   
        print("Recognising...")    
        query1=r.recognize_google(audio) # Additional command (language='en-in')
        print("User said : \n",query1) # To display the query the computer interpreted from audio output

    except Exception as e:# If the program isnt able to recognize text 
        speak("Sorry I wasnt able to catch that Say that again please...")
        return "None"    
    return query1


if __name__ == "__main__":
    wishMe() 
    print(takeCommand()) # Recognising the audio input
    while True:
        import notif
        query1 = takeCommand().lower()
        
        if 'wikipedia' in query1:
            #1.To browse data on wikipedia to access the required info given by the audio input by user
            speak("Searching Wikipedia...")
            query1 = query1.replace("wikipedia","\t")
            # Removes 'wikipedia' from the string 'query' while iterating the program
            results=wikipedia.summary(query1,sentences=2)
            # Sentences is used to operate the amt of data reproduced by the program
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'who are you' in query1:# Describes the functionality of the Virtual Desktop Assistant
            speak("I am your virtual desktop assistant created by V Suki Perumal, Sohini Kayal, Aparajitha , Using python modules and packages and integrated in Visual Studio Code , What shall I do for you !")

        elif 'simulator' in query1:# Query to run the Covid-19 Visual Simulator
            speak(" The Visual Simulator of the spread of Omicron will be displayed")
            simulator.main()
            
        elif 'cases' in query1:# Query to enable the notification system with the details of Omicron Cases
            speak("Today's Omicron Cases in India will appear on your screen ")
            def cases():

                def notifyMe(title,message):
                    notification.notify(
                        title = title,
                        message = message,
                        app_icon = "C://Users//Pesankar//OneDrive//Desktop//CompProject//image.ico",
                        timeout = 15
                    )

                def getData(url):
                    r = requests.get(url)
                    return r.text


                if __name__ == "__main__":
                    # notifyMe("Suki ","Covid-19 Daily state-wise updates")
                    
                    myHtmlData = getData("https://web.archive.org/web/20200322141055/https://www.mohfw.gov.in/")
                    soup = BeautifulSoup(myHtmlData, 'html.parser')
                    # print(soup.prettify)
                    myDataStr = ""
                    for tr in soup.find_all('tbody')[1].find_all('tr'):
                        myDataStr += tr.get_text()
                    myDataStr=myDataStr[1:]
                    itemList=myDataStr.split('\n\n')
                    states=['Karnataka','Delhi','Andhra Pradesh','Bihar','Rajasthan']
                    for item in itemList[0:23]:
                        dataList=item.split('\n')
                        if dataList[1] in states:
                            print(dataList)
                            nTitle=" Today's Omicron Cases In India "
                            nText= f"State {dataList[1]}\nIndian Nationals: {dataList[2]}Foreign nationals:{dataList[3]}\nCured: {dataList[3]}\nDeaths: {dataList[5]}"
                            notifyMe(nTitle,nText)
                            time.sleep(2)

            cases ()


        elif 'open youtube' in query1:
            # Using the webbrowser module to access youtube based on user audio input
            webbrowser.open("youtube.com")

        elif 'hello coco' in query1:
            print("Hello Suki")
            speak("Hello Suki , Hope you had a good day today !")
            speak("What shall I do for you?")

        elif 'what can you do' in query1:
            # Alternate Query for Virtual Assistant functionality
            speak("I can do the following for you suki.")
            speak("""
1. Tell the date & time 
2. Locate any place in the world on google maps
3. Instant access to youtube
4. Google/ Web browser search
5. Wikipedia results 
6. Immediate answers for all mathematical calculations and questions
7. Change my name 
8. Log off and sign out
9. Tell jokes
10. Weather of any city at any point in time 
11. Daily news                 
""")
            speak("""
My newly added covid features are : 
A Pandemic Simulator and An Omicron cases update notification system 
""")
            speak(" So what can I do for you today Suki ?")
            

        elif "change name" in query1:
            # Query to rename the Voice Assistant
            speak("What would you like to call me?")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif 'open google' in query1: 
            # Using the webbrowser module to access google based on user audio input
            webbrowser.open("google.com")

        elif 'open microsoft' in query1:
            # Using the webbrowser module to access Microsoft official website based on user audio input
            webbrowser.open("microsoft.com")        
        
        elif 'time' in query1: #6
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            # Greets the user and then informs the user on the time at that moment/
            speak("Suki, the time is: ")
            speak(strTime)
        
        elif 'shutdown system' in query1:
            # Query to shutdown the system or the Voice Assistant
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')
        
        elif "log off" in query1 or "sign out" in query1:
            # Alternate Query to shutdown the system or the Voice Assistant
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
       
        
        elif 'where is' in query1: 
            # Location Query displays the google maps link to the location mentioned in the audio input
            query1=query1.split(" ")
            location_url="https://www.google.com/maps/place/" + str(query1[2])
            maps_arg = '/usr/bin/open -a "/Applications/Google Chrome.app"'+location_url
            os.system(maps_arg)

        elif 'search' in query1 or 'play' in query1:
            # Using the search engine to play any video or music player
            query1 = query1.replace("search","")
            query1 = query1.replace("play","")
            webbrowser.open(query1)   
            time.sleep(5) 

        elif 'joke' in query1:#9
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())   

        elif 'what is a' in query1 or 'calculate' in query1:#10 and 11
            # Using wolframalpha API to answer the query
            speak("Tell your query")
            print("Query:")
            question = takeCommand()
            app_id='R8VW63-RLTVPYETV8'
            client=wolframalpha.Client(app_id)
            res=client.query(question)
            answer=next(res.results).text 
            print("the answer is :: ",answer)
            speak("The answer is: ")
            speak(answer)


#        elif 'weather' in query1:
#           speak("Here is the weather report for Bangalore Today !")
#           webbrowser.open("accuweather.com/en/in/bengaluru/204108/hourly-weather-forecast/204108")

        
#        elif 'news' in query1:#12
#           print("*************NEWS*************")
#            speak("Here are the top headlines for Bangalore Today ")
#            webbrowser.open("timesofindia.indiatimes.com/topic/Bangalore-Times-Epaper")
            
        
        elif "don't listen "  in query1 or "stop listening" in query1: #13
            # Query to put the Virtual Assistant to sleep 
            speak("As you wish Sir will be back after a while")
            time.sleep(5)


        elif 'goodbye'  in query1:#14
            # To stop the while true loop to end the program successfully based on user audio input
            print("Thank you !")
            speak("Thank you Have a great day ! ")
            # Displays this message to inform the user about the status of the program
            break   

        elif 'explain' in query1: #15
            speak("Our VA is a user-friendly and more enjoyable way to navigate the web and use our PCS. Since it is a simple python file, it can run across all platforms with the installation of the file. Thus, it is a versatile and useful program to make our online experiences more fruitful! We hope that our project aids its users and that they enjoy using our Virtual Assistant. ")
        
        else:
            pass 