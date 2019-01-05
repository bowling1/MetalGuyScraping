from requests import get
from bs4 import BeautifulSoup
import csv
from time import sleep
from time import clock
from numpy import mean

def find_duplicate(tags):
	return list(set(tags))

def is_good_response(url):
	response = get(url)
	if response.status_code == 200:
		return True
	else:
		return False

def find_rating(url):
	for i in range(1,len(url)):
		if url[i:i+4] == "/5.0":   # A couple reviews end in "X/5" instead of "X/5.0"
			if url[i-3] == ".":
				return url[i-4:i]  # This is combat ratings that are two decimal places
				break
			else:
				return url[i-3:i]
				break
#t0 = clock()  # This is to check program runtime
pagenum = 1 # Where the iteration starts. In the final test, 1.
x=0
name_list = [] # List of links to the names of the albums (will be called "<ALBUM NAME> review")
rate_list = [] # List of ratings
tags_list = []
date_list = []
genre_pre_list = []
author_pre_list = []
date_pre_list = []
genre1_list = []
genre2_list = []
genre3_list = []
author_list = []
#time_list = []

while x==0:
	# Each time this loop iterates, it checks the next page of reviews
	url = "https://www.angrymetalguy.com/category/reviews/page/" + str(pagenum) + "/"
	pagenum +=1
	# -------------------------------------------
	# Checks to see if the website exists (should iterate 407 times)
	if pagenum > 406:
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
		sleep(1.42) #seconds
		html_rating = BeautifulSoup(get(link_list[i]).text,"html.parser")
		html_string = str(html_rating)
		rate1 = find_rating(html_string)
		if rate1 == None:
			rate_list.append("No rating found")
		else:
			rate_list.append(rate1)
		# --------------------------------------------
		# Puts date and genre tags into list
		tags = html_rating.find_all(rel= "tag")
		genre_pre_list = []
		date_pre_list = []
		for i in range(0,len(tags)):
			if ("20" in tags[i].get_text()) or ("19" in tags[i].get_text()):
				date_pre_list.append(tags[i].get_text())
			elif ("Metal" in tags[i].get_text()) or ("core" in tags[i].get_text()):
				genre_pre_list.append(tags[i].get_text())
		# --------------
		# Date is added to the Master List
		if len(date_pre_list)>0:
			date_pre_list = find_duplicate(date_pre_list)
			date_list.append(date_pre_list[0])
		else:
			date_list.append("Nothing")
		# --------------
		# Genre Master List is filled
		genre_pre_list = find_duplicate(genre_pre_list)
		if len(genre_pre_list) == 0:
			genre1_list.append("Nothing")
		else:
			genre1_list.append(genre_pre_list[0])
		if len(genre_pre_list) > 1:
			genre2_list.append(genre_pre_list[1])
		else:
			genre2_list.append("Nothing")
		if len(tags_list) > 2:
			genre3_list.append(genre_pre_list[2])
		else:
			genre3_list.append("Nothing")
		# --------------------------------------------
		# Puts writer into list
		author = html_rating.find(rel= "author")
		if author != None:
			author_list.append(author.get_text)
		else:
			author_list.append("Nothing")
	print(pagenum)
		#tr2 = clock()
		#time_list.append(tr2-tr1)
	#if pagenum == 408:
		#t1 = clock()
	#x = 1
	'''
tx = clock()
print("Total elapsed time is " + str((tx-t0)))
print("Average score collection time is " + str(mean(time_list)))
print("Each page is " + str(t1-t0))
print("Total Time would be about " + str((pagenum*(tx-t0))))
print(time_list)
print(rate_list)
'''

# This turns the lists into a csv file
out = csv.writer(open("Book1.csv","w"), delimiter=",", quoting=csv.QUOTE_ALL)
out.writerow(name_list)
out.writerow(rate_list)
out.writerow(author_list)
out.writerow(date_list)
out.writerow(genre1_list)
out.writerow(genre2_list)
out.writerow(genre3_list)

# Total runtime will be approximately 2.5 hours
