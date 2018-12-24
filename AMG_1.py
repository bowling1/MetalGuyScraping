from requests import get
from bs4 import BeautifulSoup

url = 'https://www.angrymetalguy.com/category/reviews/page/100/'
raw_html = get(url).text
html = BeautifulSoup(raw_html, 'html.parser')

names = html.find_all(class_="entry-title")
for i in range(1,len(names)):
	print(names[i].get_text())
