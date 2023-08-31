#html parse
import urllib.parse
import wget
import os
import random
import requests
from bs4 import BeautifulSoup

url = 'https://yandex.ru/images/search?text='  #урл яндекса поиска картинок
search_word = input('введите запрос для поиска картинок \n') #строка поиска
req = url+search_word  #поисковый запрос

print(req) #отладка

page = requests.get(req)
#print(page.status_code)  #отладка

soup = BeautifulSoup(page.text, 'html.parser')
#print(soup) #отладка
#print(type(test))  #отладка

str_soup = str(soup.find_all('a', class_='serp-item__link')) #ищем суп и конвертим в строку
url_list = []  #список ссылок на картинки
img_count = int(str_soup.count('img_url='))  #подсчет картинок на странице
#print(img_count) #отладка

#наполнение списка урл
for i in range(img_count):
	left = str_soup.find('img_url=') + 8 #начало урл картинки
	str_soup = str_soup[left:]  #отрезаем мусор с начала строки
	right = str_soup.find('&amp;') #конец урл картинки
	url_list.append(str_soup[:right]) #пополняем список урлов
	str_soup = str_soup[right:] #отрезаем отработанное

#обработка списка урл
for i in range(len(url_list)):
	url_list[i] = urllib.parse.unquote(url_list[i])

print('\n\n\n')
dl_file_url = random.choice(url_list)
print(dl_file_url)

print('try to dl file\n')
if(os.path.isfile(search_word + '.jpg')):
	os.remove(search_word + '.jpg')
	
wget.download(dl_file_url, search_word + '.jpg')
print('\n file downloaded')

#input()
