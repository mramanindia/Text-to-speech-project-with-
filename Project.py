import PyPDF2
import os
from gtts import gTTS 
path = open('api.pdf', 'rb')

#Now we haveto sysc through the pdf...
#we are calling the pdf file to the pdfreader for extracting the content
pdfReader = PyPDF2.PdfFileReader(path)

#we are navigating throgh the page 
from_page = pdfReader.getPage(0)

#extracting the text from the pdf ....
Pagedata = from_page.extractText()

#we are sending the data to the google api and from there it is doing the mp3 converting thing for us
speech = gTTS(text = Pagedata, lang = 'en', slow = True) 
#after that with the help of speech we are saving it in the local folder
speech.save('text.mp3')
#we are callin os to start our mp3 file 
os.system("start text.mp3")