from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random


"""получить произвольную страницу «Википедии» и
создать список ссылок, присутствующих на этой странице"""

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
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
random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen(f'http://en.wikipedia.org{articleUrl}')
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/Kevin_Bacon')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)