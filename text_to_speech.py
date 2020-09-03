from gtts import gTTS
import os

print("Tamizhuku En Ondrai Azhuthavum")
print("press 2 for English: ")
l2s=input()
if (ls==1):
    lans='ta'
else:
    lans = 'en'

st=input("enter text to convert into speech: ")

myobj=gTTS(text=st, lang=lans,slow=False)
myobj.save("welcome.mp3")

os.system("start welcome.mp3")