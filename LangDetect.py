from googletrans import Translator, constants
from pprint import pprint

trans=Translator()

print("Enter Pharse to Detect Language")

inp=str(input())

detection=trans.detect(inp)

print("Language:", constants.LANGUAGES[detection.lang])
print("Language code:", detection.lang)
print("Confidence:", detection.confidence)
