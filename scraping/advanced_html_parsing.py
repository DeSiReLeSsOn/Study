from urllib.request import urlopen
from bs4 import BeautifulSoup
#html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
#bs = BeautifulSoup(html, 'html.parser')
#print(bs)

#nameList = bs.find_all('span', {'class': 'green'})
#for name in nameList:
#    print(name.get_text())



#titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
#print([title for title in titles])



#allText = bs.find_all('span', {'class':{'green', 'red'}}) # функция ищет в HTML-документе теги span с классом green или red
#print([text for text in allText])


#nameList = bs.find_all(string='the prince') # узнать, сколько раз на странице встречается слово the prince, заключенное в  теги
#print(len(nameList))


#title = bs.find_all(id='title', class_='text') # выбрать теги, содержащие определенный атрибут или набор атрибутов
#print([text for text in allText]) # Этот код возвращает первый тег со словом text в атрибуте class_ и словом title в атрибуте id. 


"""Данный код выводит список всех строк таблицы giftList,
в том числе начальную строку с заголовками столбцов.
Если
вместо функции children() в этом коде использовать
функцию desndants(), то она найдет в таблице и выведет
примерно два десятка тегов, включая img, span и отдельные
теги td. 
"""
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
for child in bs.find('table',{'id':'giftList'}).children:
    print(child)