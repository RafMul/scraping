# -*- coding: utf-8 -*-
import requests
from  bs4 import BeautifulSoup




url = "http://www.rzeszowiak.pl/Nieruchomosci-Sprzedam-3070011155?r=domy"
page = requests.get(url)
s = page.text
soup = BeautifulSoup(s,'lxml')

title =soup.find_all('div','promobox-title-left')

cena = soup.find_all('div','promobox-title-left2')


adressDIV = soup.find_all("div", attrs= {'class': 'promobox-title-left' })
adress = []																	# Tablica class promobox-title-left z adresami
																			# Tablica nezbędna do poprania adresów wwww
for a in  adressDIV:
	adress.append(a)										# Dodawanie clas promobox-title-left do tablicy


add_title_page = []
link_title = []												# Tablica z href  sam link
for n in adress:
	a_tag = n.find('a', href=True)
	href = a_tag['href']
	add_title_page.append("http://www.rzeszowiak.pl")
	link_title.append(href)										# Dodawanie do tablicy href link

page_link = []												# lista linków do stron z ofertą
for li, ja in zip (add_title_page,link_title) :
	ge = li + ja
	page_link.append(ge)										# dodawanie dwoch tablic i generowanie linku

title_list = []												# Tablica z tytułami class promobox-title-left text
cena_list = []												# Tablica z canami class promobox-title-left2

for titles in title:
	title_list.append(titles.getText().split('/n')[0])						# Dodawanie do tablicy tytułów
for cen in cena:
	cena_list.append(cen.getText().split('/n')[0])							# Dodawanie do tablicy cen


f1 = open("scraping.txt","w")

razem = []
for title, cena, adress in zip (title_list,cena_list,page_link):
	r = title +'  |  '+cena +'  |  '+ adress
	razem.append(r)
for i in (razem):
	f1.write(i+'\n')
	#f1.write('\n')
	#f1.write('\n')
	print(i)
f1.close()
