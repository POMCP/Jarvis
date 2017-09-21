import speech_recognition as sr
import wolframalpha
from os import system
import requests
from googletrans import Translator
import sys


translator = Translator()
r = sr.Recognizer()
m = sr.Microphone()
reload(sys)
sys.setdefaultencoding('utf-8')

'''def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def google_results(query):
    service = build("customsearch", "v1",
                    developerKey="devkey")

    result = service.cse().list(
            q=query, cx="cseKey").execute()
    return cleanhtml(result["items"][00]["htmlSnippet"])'''

# Wolfram Api
app_id = "wolframAPIkey"
client = wolframalpha.Client(app_id)
run = False
sleep = True
greeting=True

try:
    print("A moment of silence, please...")
    with m as source:
        r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))

    while sleep:
        print('Say Hallo to bring me to life...')
        with m as source:audio = r.listen(source)
        #print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio, language="de_DE")

            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                print(u"You said {}".format(value).encode("utf-8"))
            else:  # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(value))

            if 'Hallo' in value:
                run = True
                system('say -v Anna ' + translator.translate('Hello, how are you today?', dest='de').text) #Here is the
                # speaking part
                #speech_engine.runAndWait()

        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))

        while run:
            print("Say something!")
            with m as source: audio = r.listen(source)
            print("Got it! Now to recognize it...")
            try:
                # recognize speech using Google Speech Recognition
                value = r.recognize_google(audio, language="de_DE")

                if 'wiedersehen' in value:
                    sleep = False
                    run = False
                    system('say -v Anna Auf wiedersehen')  # Here is
                    #  the
                    # speaking
                    # part
                    #speech_engine.runAndWait()
                    continue

                # we need some special handling here to correctly print unicode characters to standard output
                if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                    print(u"You said {}".format(value).encode("utf-8"))
                else:  # this version of Python uses unicode for strings (Python 3+)
                    print("You said {}".format(value))

                '''Here comes the code to react to the user answer about their well being'''
                if greeting:
                    data = [
                        ('text', translator.translate(value, dest='en').text)
                    ]

                    resp1 = requests.Session().post('http://text-processing.com/api/sentiment/', data=data)
                    resp1 = resp1.json()
                    print(resp1)

                    label = resp1.get("label")
                    if label == "neg":
                        system('say -v Anna ' + translator.translate('Sorry to hear that, hope you get better!',
                                                                     dest='de').text)
                    elif label == "pos":
                        system('say -v Anna ' + translator.translate('Good to hear that!', dest='de').text)
                    elif label == "neutral":
                        system('say -v Anna ' + translator.translate('Good to hear from you!', dest='de').text)
                    greeting = False
                    continue

                '''Here comes the code to respond if asked how the tree is'''
                if 'Wie geht es dir' in value:
                    humidity = 1
                    temperature = 25
                    system('say -v Anna ' + translator.translate('The humidity around me is' + str(humidity) + ' and the temperature is a pleasant ' + str(temperature) + ' degrees. I feel great!', dest='de').text)
                    continue

                value = translator.translate(value, dest='en').text
                #Query the Wolframalpha client
                params = (
                    ('i', value),
                    ('appid', '3P2YJL-Q8A29JJ674'),
                )
                resp = requests.Session().get('http://api.wolframalpha.com/v1/result', params=params)
                print(resp.text)
                system('say -v Anna ' + translator.translate(resp.text, dest='de').text)

            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
            #run = False
except KeyboardInterrupt:
    pass
