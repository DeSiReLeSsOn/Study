from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html, 'html.parser')
#print(bs)

nameList = bs.find_all('span', {'class': 'green'})
#for name in nameList:
#    print(name.get_text())



#titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
#print([title for title in titles])



allText = bs.find_all('span', {'class':{'green', 'red'}})
print([text for text in allText])