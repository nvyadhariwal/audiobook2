

import pyttsx3
import PyPDF2
from tkinter.filedialog import *


engine = pyttsx3.init()
rate = engine.getProperty("rate")
engine.setProperty("rate",150)
print(rate)


voices = engine.getProperty("voices")
print("Male Voice : {0}".format(voices[0].id))
print("Female Voice : {0}".format(voices[1].id))

engine.setProperty("voice", voices[1].id)



book = askopenfilename()
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages

for num in range(0, pages):
    page = pdfreader.getPage(num)
    text = page.extractText()
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()





