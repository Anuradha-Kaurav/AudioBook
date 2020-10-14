import pyttsx3
import PyPDF2

book = open('Introduction_to_Machine_Learning.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
audio = pyttsx3.init()
pages = pdfReader.numPages

for num in range(5, pages):
    singlePage = pdfReader.getPage(num)
    text = singlePage.extractText()
    audio.say(text)
    audio.runAndWait()