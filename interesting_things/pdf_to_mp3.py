#установим необходимые библиотеки pip install gtts, pip install PyPDF2
from gtts import gTTS
import PyPDF2

#Путь к файлу
pdf_File = open('name.pdf', 'rb') 

#Создадим PDF-reader 
pdf_Reader = PyPDF2.PdfFileReader(pdf_File)
count = pdf_Reader.numPages # counts number of pages in pdf
textList = []

#Извлечем текс для каждой страницы PDF-файла
for i in range(count):
   try:
    page = pdf_Reader.getPage(i)    
    textList.append(page.extractText())
   except:
       pass

#Преобразуем многострочный текс в однострочный
textString = " ".join(textList)

print(textString)

#устновим язык
language = 'ru'

#обратимся к  GTTS
myAudio = gTTS(text=textString, lang=language, slow=False)

#Сохраним файл в формате mp3
myAudio.save("Audio.mp3")
