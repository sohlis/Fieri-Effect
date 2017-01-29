#Import required modules and packages (proper nomenclature unknown)
import pandas as pd
from bs4 import BeautifulSoup
import os
import urllib
import mechanize

#Set working directory to where csv file is located
os.chdir("/Users/buchman/Documents/rproject/Fieri-Effect")

#Read in csv file of restaurant names
#search_list = pd.read_csv("data_for_url_scraper.csv", sep=',', skiprows=1)


#Code from tutorial video on searching google with python 

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders= [('User-agent', 'chrome')]

term = "Mac & Ernie's Tarpley Texas yelp".replace(" ", "+")

query = "http://www.google.com/search?q="+term+"&oq="+term

htmltext = br.open(query).read()
#print(htmltext)

soup = BeautifulSoup(htmltext)

search = soup.findAll('div', {'class' : 'rc'})

#print(search)
# : {'class': 'r'}
for item in search:
	print item.contents[0].findAll('a')[0].txt