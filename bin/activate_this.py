import speech_recognition as sr
import random
import os
os.environ['TERM'] = 'xterm'
import webbrowser
import replicate
from sympy import sympify
import datetime
import time
from config import REPLICATE_API_TOKEN

client = replicate.Client(api_token=REPLICATE_API_TOKEN)


def chat_with_ai(prompt):
    try:
        print("Thinking...")
        output = client.predictions.create(
            version = "mistralai/mixtral-8x7b-instruct-v0.1",
            input = {"prompt": prompt}
        )
        return output.output or "I'm not sure how to respond to that."
    except Exception as e:
        print(f"Error: {e}")
        return "I couldn't process your request. Please try again later."


def say(text):
    if text:
        os.system(f"say '{text}'")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            print("Recognising...")
            query = r.recognize_google(audio, language = "en-in")
            print(f'User said: {query}')
            return query
        except Exception as e:
             return "Some error occurred. Sorry from MINI JARVIS A.I!"
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that. Could you repeat?"
        except sr.RequestError as e:
            return "There seems to be an issue with the speech service."



if __name__ == "__main__":
    say("Hello I am MINI JARVIS A.I")
    while True:
        print("Listening...")
        query = take_command()
        sites = [["Youtube", "https://www.youtube.com/"],["Google", "https://www.google.com/"],
                 ["lead code","https://leetcode.com/"]] #add more sites
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                webbrowser.open(site[1])
                say(f"Opening {site[0]}....")

    #todo:add apps to use from the mac use pwd command to copy there path
        apps = [["Whatsapp", "/Applications/WhatsApp.app"],["Chatgpt","/Applications/ChatGPT.app"],
                ["Facetime","/System/Applications/FaceTime.app"],["VS Code","/Applications/Visual Studio Code.app"],
                ["Chrome","Applications/Google Chrome.app"],["Spotify","/Applications/Spotify.app"]]
        for app in apps:
            if f"Open {app[0]}".lower() in query.lower():
                os.system(f"open {app[1]}")
                say(f"Opening {app[0]}....")

    #todo:open specific apps especially the music app
        if 'open music' in query:
            musicPath = "/Applications/Spotify.app"
            os.system(f"open {musicPath}")

    # tells the time
        if 'the time' in query:
             hour = datetime.datetime.now().strftime("%H")
             min = datetime.datetime.now().strftime("%M")

             say(f"Bhai time hey {hour} {min}!")

    #todo:open ai or voice assistant from my Mini JARVIS
        if 'siri'.lower() in query.lower():
            os.system(f"open /System/Applications/Siri.app")

    #todo:special custom messages
        if 'I love you' in query:
            say("I love You too Darling...!")


    #todo:add some people special message for them! :)
        # Explosion Effect
        def explosion_effect():
            explosion = [
                "   *   ",
                "  ***  ",
                " ***** ",
                "*******",
                " ***** ",
                "  ***  ",
                "   *   "
            ]
            for frame in explosion:
                print(frame.center(40))
                time.sleep(0.2)
            print("Boom! 💥")

        if 'hello I am Ritik' in query:
            explosion_effect()
            say("Hey! So you are the great fake Attri")


        # def emoji_rain(emojis=["😳", "😊", "🤩","☀️","🌧️","❄️"], lines=10):
        #     for _ in range(lines):
        #         line = ''.join(random.choice(emojis) for _ in range(30))
        #         print(line)
        #         time.sleep(0.1)
        #
        # if "I am " in query:
        #     # emoji_rain()
        #     say("Oh! How are You?")


    #todo:making of ai interactive and do some works own it own through tokens....
        if "calculate" in query:
            try:
                expression = query.replace("calculate", "").strip()
                result = sympify(expression)
                say(f"The result is {result}")
            except Exception as e:
                say("Sorry, I couldn't calculate that.")

        if 'write email' in query or 'talk' in query:
            say("What should I write or talk about?")
            user_prompt = take_command()
            response = chat_with_ai(user_prompt)
            say(response)
            print(f"AI Response: {response}")


    #todo:add words for exiting!
        if any(keyword in query.lower() for keyword in ["namaskar", "quit", "exit", "goodbye", "bye", "terminate", "namaste", "नमस्कार"]):
            for char in "We will meet again! \U0001F608\n":
                print(char, end="", flush = True) # typewriter effect
                time.sleep(0.05) #Ajust for slower/faster effect
            say("Titanic sinking !!")
            break
        # say(query)
