from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
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
#html = urlopen('http://www.pythonscraping.com/pages/page3.html')
#bs = BeautifulSoup(html, 'html.parser')
#for child in bs.find('table',{'id':'giftList'}).children:
#    print(child)

"""Этот код должен выводить все строки таблицы, кроме
первой с заголовком."""
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
#for sibling in bs.find('table', {'id':'giftList'}).tr.next_siblings:
#    print(sibling)

"""Этот код будет выводить цену объекта, изображенного на
картинке ../img/gifts/img1.jpg (в данном случае цена
составляет 15 долларов).
"""
#print(bs.find('img', {'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())

"""Этот код выводит только те относительные пути к
изображениям, которые начинаются с ../img/gifts/img и
заканчиваются на .jpg"""
images = bs.find_all('img', {'src':re.compile('..\/img\/gifts/img.*.jpg')})
#for image in images:
#    print(image['src'])

"""следующая функция возвращает все теги,
имеющие ровно два атрибута"""
print(bs.find_all(lambda tag: len(tag.attrs) == 2))


#находит тег с текстом 'Or maybe he\'s only resting?'
print(bs.find_all(lambda tag: tag.get_text() == 'Or maybe he\'s only resting?'))
#То же самое можно выполнить и без лямбда-функции
print(bs.find_all('', text='Or maybe he\'s only resting?'))
