import speech_recognition as sr
import pyttsx3
import webbrowser
import musichub
import requests

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


my_news_api="576d17d6dc06474c9ed45959b71431f5"


def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com/amir-gurung08")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open gmail" in c.lower():
        webbrowser.open("https://gmail.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musichub.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=np&apiKey={my_news_api}")
        
            # Check if request was successful
        if r.status_code == 200:
           #parse the json response
           data = r.json()

           #extract the articles
           articles = data.get("articles",[])

           #speak the headlines
           for article in articles:
               speak(article["title"])


    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't understand that command.")


if __name__ == "__main__":
    speak("Initializing Brother.....")

    #Listen For the wake word Hero
    #obtain audio from microphone
    while True:
        #recognize speech using google
        print("Recognizing wake word...")
        try:

            with sr.Microphone() as source:
                 r.adjust_for_ambient_noise(source)
                 print("Listening for wake word...")
                 audio = r.listen(source, timeout=5, phrase_time_limit=2)
            word = r.recognize_google(audio)
            print("Heard:", word)
            if word.lower() == "brother":
                speak("Yes, I'm listening.")

                #listen for command
                with sr.Microphone() as source:
                    print("Listening for your command...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=2)
                    command = r.recognize_google(audio)
                    print("Command received:", command)
                    processcommand(command)
        except sr.WaitTimeoutError:
            print("Listening timed out, waiting again...")
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except Exception as e:
            print(f"Error: {e}")
            speak("Sorry, I encountered an error.")
            