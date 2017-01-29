#Import required modules and packages (proper nomenclature unknown)
import pandas as pd
from bs4 import BeautifulSoup
import os
import urllib
import mechanize
import re
import csv

#Set working directory to where csv file is located
os.chdir("/Users/buchman/Documents/rproject/Fieri-Effect")

#Read in csv file of restaurant names
with open('data_for_url_scraper.csv', 'rb') as f:
   reader = csv.reader(f)
   your_list = list(reader)

#Make sure google knows we are chill bros and not robots
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders= [('User-agent', 'chrome')]

your_list1 = your_list[1:10]

for item in your_list1:
    test_term = str(item)

    term = test_term.replace(" ", "+")

    encoded = urllib.quote(term)

    query = "http://www.google.com/search?q="+encoded

    htmltext = br.open(query).read()

    soup = BeautifulSoup(htmltext, "html.parser")

    search = soup.findAll('div',attrs={'id':'search'})

    searchtext = str(search[0])

    regex = "q(?!.*q).*?&amp"
    pattern = re.compile(regex)

    soup1 = BeautifulSoup(searchtext, "html.parser")
    list_items = soup1.findAll('a')

    source_url = str(re.findall(pattern, str(list_items[0])))

    source_url_final = source_url.replace("q=", "").replace("&amp", "")

    print(source_url_final)


