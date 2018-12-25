from requests import get
from bs4 import BeautifulSoup

url = "https://www.angrymetalguy.com/category/reviews/page/36"
raw_html = get(url).text
html = BeautifulSoup(raw_html, "html.parser")
names = html.find_all(class_="entry-title")

#print(html.prettify())
#print(names)
link_list = []
link = names[0].find('a')
print(link.attrs['href'])
for i in range(0,len(names)):
	link1 = names[i].find('a')
	link2 = link1.attrs['href']
	link_list.append(link2)

print(link_list)
	
