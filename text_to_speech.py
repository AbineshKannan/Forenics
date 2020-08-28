from gTTS import gTTS
import os

mytext="Hello"
langs ='en'

myobj=gTTS(text=mytext, lang=langs,slow=False)
myobj.save("welcome.mp3")

os.system("mpg321 welcome.mp3")