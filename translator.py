from googletrans import Translator, constants
from pprint import pprint

trans=Translator()

print("Enter Text to Translate")

ip=input()

translation = trans.translate(ip,dest = "ta")
print(f"{translation.origin}  ({translation.src}) --> {translation.text} ({translation.dest})")
