import os
import sys
import pyttsx3
import datetime
import cv2
import random
import wikipedia
import webbrowser
import smtplib
import pywhatkit as kit
from requests import get
import speech_recognition as sr  

engine = pyttsx3.init('sapi5')  
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Text to Speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    
# To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=3, phrase_time_limit=7) 
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in').lower()  
        print(f"User said: {query}")
        
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand. Please say that again.")
        return ""
    except sr.RequestError:
        speak("Network issue. Please check your connection.")
        return ""
    except Exception as e:
        speak("Say that again please.")
        return ""
    
    return query

# To Wish
def wish():
    hour = int(datetime.datetime.now().hour)
    
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 14:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("My name is Jarvis, I am your Personal AI Assistant, how may I help you?")

def play_music():
    music_dir = "D:\\MUSIC"
    songs = [song for song in os.listdir(music_dir) if song.endswith('.mp3')]
    random.shuffle(songs)  
    for song in songs:
        os.startfile(os.path.join(music_dir, song))
        
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your-email@gmail.com', 'your-app-password')  # Use App Password
    server.sendmail('your-email@gmail.com', to, content)
    server.close()
    
if __name__ == "__main__":
    wish()
    
    while True:
        query = takecommand().lower()
        
        if "open notepad" in query:
            os.startfile("C:\\Windows\\notepad.exe")
        
        elif "open vscode" in query:
            os.system("code")  # Universal method to open VS Code
            
        elif "open command prompt" in query:
            os.system('start cmd') 
        
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                if cv2.waitKey(50) & 0xFF == 27:  # Press ESC to exit
                    break
            cap.release()
            cv2.destroyAllWindows()
            
        elif "play music" in query:
            play_music()
                    
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP Address is: {ip}")
            
        elif "wikipedia" in query:
            speak("Searching Wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)
            
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
            
        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")
        
        elif "open stack overflow" in query:
            webbrowser.open("www.stackoverflow.com")
            
        elif "open google" in query:
            speak("What should I search on Google?")
            cm = takecommand().lower()
            if cm == "":
                webbrowser.open("www.google.com")
            else:
                webbrowser.open(f"https://www.google.com/search?q={cm}")
            
        elif "send message" in query:
            now = datetime.datetime.now()
            kit.sendwhatmsg("+919702002320", "Greetings from Raghav", now.hour, now.minute + 2)
            
        elif "play song on youtube" in query:
            speak("Which song should I play?")
            song_name = takecommand().lower()
            kit.playonyt(song_name)
            
        elif "email to krish" in query:
            try:
                speak("What should I say?")
                content = takecommand().lower()
                to = "EMAIL OF THE OTHER PERSON"
                sendEmail(to, content)
                speak("Email has been sent to Krish")
                
            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to send this email to Krish")
        
        elif "set alarm" in query:
            nn =int (datetime.datetime.now().hour)
            if nn==22:
                music_dir = ''
                
        elif "no" in query:
            speak("Thank you, have a good day")
            sys.exit()            
        
        speak("Do you have any other work, sir?")            
        