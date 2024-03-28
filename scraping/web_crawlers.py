from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random


"""получить произвольную страницу «Википедии» и
создать список ссылок, присутствующих на этой странице"""

#html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
#bs = BeautifulSoup(html, 'html.parser')
#for link in bs.find_all('a'):
#    if 'href' in link.attrs:
#        print(link.attrs['href'])
"""получим список всех URL статей, на
которые ссылается статья «Википедии» о Кевине Бейконе"""
#for link in bs.find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')):
#    if 'href' in link.attrs:
#       print(link.attrs['href'])


"""Сразу после импорта необходимых библиотек программа
присваивает генератору случайных чисел начальное значение,
равное текущему системному времени, чем обеспечивает
новый и интересный случайный путь по статьям «Википедии»
практически при каждом запуске программы"""
#random.seed(datetime.datetime.now())
#def getLinks(articleUrl):
#    html = urlopen(f'http://en.wikipedia.org{articleUrl}')
#    bs = BeautifulSoup(html, 'html.parser')
#    return bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))

#links = getLinks('/wiki/Kevin_Bacon')
#while len(links) > 0:
#    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
#    print(newArticle)
#    links = getLinks(newArticle)


"""Веб-скрапер не
ограничивается только страницами статей, а ищет все ссылки,
начинающиеся с /wiki/, независимо от того, где они
располагаются на странице и содержат ли двоеточия.
Изначально функция getLinks вызывается с пустым URL,
то есть для начальной страницы «Википедии»: к пустому URL
внутри функции добавляется http://en.wikipedia.org.
Затем функция просматривает каждую ссылку на первой
странице и проверяет, есть ли она в глобальном множестве
страниц (множестве страниц, с которыми скрипт уже
встречался). Если нет, то ссылка добавляется в список,
выводится на экран и функция getLinks вызывается для нее
рекурсивно.

"""
#pages = set()
# def getLinks(pageUrl):
#     global pages     
#     html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
#     bs = BeautifulSoup(html, 'html.parser')
#     for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
#         if 'href' in link.attrs:
#             if link.attrs['href'] not in pages:
#                 # мы нашли новую страницу
#                 newPage = link.attrs['href']
#                 print(newPage)
#                 pages.add(newPage)
#                 getLinks(newPage) 

#getLinks('')





"""Цикл for в этой программе, по сути, такой же, как и в
первоначальной программе сбора данных (для ясности
добавлен вывод дефисов в качестве разделителей контента).
Поскольку никогда нельзя быть полностью уверенными в
том, что на каждой странице будут присутствовать все нужные
данные, операторы print расположены в соответствии с
вероятностью наличия этих данных на странице. Так, тег
заголовка h1 есть на каждой странице (во всяком случае,
насколько я могу судить), вследствие чего мы сначала
пытаемся получить эти данные. Текстовый контент
присутствует на большинстве страниц (за исключением
страниц файлов), так что этот фрагмент данных извлекается
вторым. Кнопка редактирования есть только на страницах с
заголовками и текстовым контентом, и то не на всех."""
pages = set()
def getLinks(pageUrl):
    global pages 
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    try:
        print(bs.find(id='mw-content-text').find_all('p')[0])
        print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('This page missing something! Continuing')  
        for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
            if 'href' in link.attrs:
                if link.attrs['href'] not in pages:
                    # мы нашли новую страницу
                    newPage = link.attrs['href']
                    print('-'*20)
                    print(newPage)
                    pages.add(newPage)
                    getLinks(newPage)   

getLinks('')