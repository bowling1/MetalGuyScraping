from requests import get
from bs4 import BeautifulSoup
import csv
from time import sleep
#from time import clock
#from numpy import mean


def is_good_response(url):
	response = get(url)
	if response.status_code == 200:
		return True
	else:
		return False

def find_rating(url):
	html_rating = BeautifulSoup(get(url).text,"html.parser")
	html_string = str(html_rating)
	for i in range(1,len(html_string)):
		if html_string[i:i+4] == "/5.0":   # A couple reviews end in "X/5" instead of "X/5.0"
			if html_string[i-3] == ".":
				return html_string[i-4:i]  # This is combat ratings that are two decimal places
				break
			else:
				return html_string[i-3:i]
				break
# t0 = clock()  # This is to check program runtime
pagenum = 403 # Where the iteration starts. In the final test, 1.
x=0
name_list = [] # List of links to the names of the albums (will be called "<ALBUM NAME> review")
rate_list = [] # List of ratings
#time_list = []

while x==0:
	# Each time this loop iterates, it checks the next page of reviews
	url = "https://www.angrymetalguy.com/category/reviews/page/" + str(pagenum) + "/"
	pagenum +=1
	# -------------------------------------------
	# Checks to see if the website exists (should iterate 407 times)
	if pagenum > 405
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
	# -------------------------------------------
	# Check the reviews for the score, and puts it in a list	
	
	for i in range(0, len(link_list)):
		#tr1 = clock()
		sleep(1.7) #seconds
		rate1 = find_rating(link_list[i])
		if rate1 == None:
			rate_list.append("No rating found")
		else:
			rate_list.append(rate1)
		#tr2 = clock()
		#time_list.append(tr2-tr1)

'''
tx = clock()
print("Total elapsed time is " + str((tx-t0)))
print("Average score collection time is " + str(mean(time_list)))
print(time_list)
print(rate_list)
'''

# This turns the lists into a csv file
out = csv.writer(open("Book1.csv","w"), delimiter=",", quoting=csv.QUOTE_ALL)
out.writerow(name_list)
out.writerow(rate_list)


# Total runtime will be approximately 2.5 hours
