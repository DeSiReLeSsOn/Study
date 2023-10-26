# установим модуль pypdf2 командой pip3 install pypdf2
from PyPDF2 import PdfFileWriter, PdfFileReader
from getpass import getpass
pdfwriter = PdfFileWriter()
pdf = PdfFileReader('name_file.pdf') #  аргументом передаем путь к файлу который хоитим зашифровать 


for page in range(pdf.numPages):
    pdfwriter.add_page(pdf.pages[page])


password = getpass(prompt='Введите пароль: ')
pdfwriter.encrypt(password)


with open('protected.pdf', 'wb') as file: 
    pdfwriter.write(file)