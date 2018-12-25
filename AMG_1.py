from requests import get
from bs4 import BeautifulSoup
import csv


def is_good_response(url):
	response = get(url)
	if response.status_code == 200:
		return True
	else:
		return False
pagenum = 406
x=0
name_list = []

while x==0:
	url = "https://www.angrymetalguy.com/category/reviews/page/" + str(pagenum) + "/"
	if not is_good_response(url):
		x = 1
	pagenum +=1
	raw_html = get(url).text
	html = BeautifulSoup(raw_html, "html.parser")
	names = html.find_all(class_="entry-title")
	for i in range(1,len(names)):
		name_list.append(names[i].get_text())

print(name_list)

'''
with open("Book1.csv", "a") as csvFile:
	writer = csv.writer(csvFile)
	writer.writerow(name_list)

csvFile.close()

# This turns the list created into a row in a csv file
'''
