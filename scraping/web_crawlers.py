from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

"""получить произвольную страницу «Википедии» и
создать список ссылок, присутствующих на этой странице"""

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
#for link in bs.find_all('a'):
#    if 'href' in link.attrs:
#        print(link.attrs['href'])
"""получим список всех URL статей, на
которые ссылается статья «Википедии» о Кевине Бейконе"""
for link in bs.find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])