#Import required modules and packages (proper nomenclature unknown)
import numpy as np
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
#search_list = pd.read_csv("data_for_url_scraper.csv", sep=',')

#print(search_list)

#df = pd.DataFrame(search_list)

#print df[1, 1]


with open('data_for_url_scraper.csv', 'rb') as f:
   reader = csv.reader(f)
   your_list = list(reader)

print your_list[1]
