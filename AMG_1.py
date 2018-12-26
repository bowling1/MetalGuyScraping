from requests import get
from bs4 import BeautifulSoup
import csv


def is_good_response(url):
	response = get(url)
	if response.status_code == 200:
		return True
	else:
		return False

pagenum = 406 # Where the iteration starts. In the final test, 1.
x=0
name_list = [] # List of links to the names of the albums (will be called "<ALBUM NAME> review")

while x==0:
	# Each time this loop iterates, it checks the next page of reviews
	url = "https://www.angrymetalguy.com/category/reviews/page/" + str(pagenum) + "/"
	# -------------------------------------------
	# Checks to see if the website exists (should iterate 407 times)
	if not is_good_response(url):
		x = 1
	# ------------------------------------------- 
	# Creates the html of the website being iterated
	raw_html = get(url).text
	html = BeautifulSoup(raw_html, "html.parser")
	names = html.find_all(class_="entry-title")
	# -------------------------------------------
	# Creates a list of names of the albums being reviewed
	for i in range(0,len(names)):                         # There might be an error in starting at 1, maybe start at 0.
		name_list.append(names[i].get_text())			  # Using 1 might excluding the first review on each page	
	# -------------------------------------------
	# Creates a list of links of the reviews on the page being iterated
	link_list = [] # List of links to reviews. Refreshes every page loop.
	for i in range(0,len(names)):
		link1 = names[i].find('a')
		link2 = link1.attrs['href']
		link_list.append(link2)
	pagenum +=1
'''
with open("Book1.csv", "a") as csvFile:
	writer = csv.writer(csvFile)
	writer.writerow(name_list)
csvFile.close()
# This turns the list created into a row in a csv file
'''
