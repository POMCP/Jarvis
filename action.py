import speech_recognition
import pyttsx
import wolframalpha
from googleapiclient.discovery import build
import re

speech_engine = pyttsx.init()
speech_engine.setProperty('rate', 150)

# Wolfram Api
app_id = "3H4RK9-WQ63W49WWW"
client = wolframalpha.Client(app_id)
# speech_engine.say('Hello Sir, How may I help you today ?')
# speech_engine.runAndWait()


def speak(text):
    speech_engine.say(text)
    speech_engine.runAndWait()

recognizer = speech_recognition.Recognizer()


def listen():
    with speech_recognition.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        value = recognizer.recognize_google(audio)
        if str is bytes:  # this version of Python uses bytes for strings (Python 2)
            print(u"You said {}".format(value).encode("utf-8"))
            a = format(value).encode("utf-8")
        else:  # this version of Python uses unicode for strings (Python 3+)
            print("You said {}".format(value))
            a = format(value)
        return value, a
    except speech_recognition.UnknownValueError:
        print("Oops! Didn't catch that")
    except speech_recognition.RequestError as e:
        print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))

    return ""


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def google_results(query):
    service = build("customsearch", "v1",
                    developerKey="AIzaSyAeSL5HTHJcxH9SeeWfS_qf2nFWRHBc8HU")

    result = service.cse().list(
            q=query, cx="014232785313891304027:nfy0x-f7cn8").execute()
    return cleanhtml(result["items"][00]["htmlSnippet"])

running = True
run = True
print 'Listening...'
while run:
    v, a = listen()
    if a in ['hello Jarvis', 'wake up Jarvis', 'hey']:
        speak("Hello Sir, How may I help you today ?")
        break

while running:
    v, a = listen()
    if a in ['exit', 'Exit', 'quit', 'goodbye Jarvis', 'Tata', 'tata']:
        speak("Have a good day Sir!")
        break
    res = client.query(a)
    try:
        print next(res.results).text
        speak(next(res.results).text)
    except AttributeError:
        print "Oops! Didn't catch that"
        speak("Oops! Didn't catch that")
    except StopIteration:
        print "Couldn't find anything here, sorry"
        speak("Couldn't find anything here, sorry")
    except KeyError:
        speak("Oops!, I am afraid I didn't catch that Sir")
    except:
        print "Something went wrong, Try again"
        speak("I am not sure what happened. Please try again")
    # speak("I heard you say " + v)
    print "Ready!"

    '''g_res = google_results(a)
    try:
        print g_res
        speak(g_res)
    except AttributeError:
        print "Oops! Didn't catch that"
        speak("Oops! Didn't catch that")
    except StopIteration:
        print "Couldn't find anything here, sorry"
        speak("Couldn't find anything here, sorry")
    except KeyError:
        speak("Oops!, I am afraid I didn't catch that Sir")
    except:
        print "Something went wrong, Try again"
        speak("I am not sure what happened. Please try again")
        # speak("I heard you say " + v)
    print "Ready!" '''
