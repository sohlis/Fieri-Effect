#Import required modules and packages (proper nomenclature unknown)
import pandas as pd
from bs4 import BeautifulSoup
import os
import urllib
import re
import csv
import requests


#Set working directory to where csv file is located
os.chdir("/Users/gerikillo/Desktop/Effect_url_list")

#Read in csv file of restaurant names
with open('data_for_url_scraper.csv', 'rb') as f:
   reader = csv.reader(f)
   your_list = map(tuple, reader)

your_list1 = your_list


list_of_urls = []
list_of_names = []

print("Working on your stupid ass query...")

for item in your_list1:
    test_term = str(item)
    
    test_term_final = test_term.replace("('", "").replace("',)", "").replace("(\"","").replace("\",)","").replace("\\","").replace("x92xa9","e")                                                                                                                                                     
    
    term = test_term_final.replace(" ", "+").replace("x8ax97xc8","\'").replace("xe4xf3xf1","")      

    encoded = urllib.quote(term)

    query = "http://www.google.com/search?q="+encoded
 
    requestsinfo = requests.get(query)

    htmltext = requestsinfo.content

    soup = BeautifulSoup(htmltext, "html.parser")

    search = soup.findAll('div',attrs={'id':'search'})

    searchtext = str(search[0])

#find the link
    regex = "q=(?!.*q=).*?&amp"
    pattern = re.compile(regex)
    
    soup1 = BeautifulSoup(searchtext, "html.parser")
    list_items = soup1.findAll('a')

#check for errors and makes sure the link contains 'yelp.com/biz/'
    try:
        for x in range(0,10):
            source_url = str(re.findall(pattern, str(list_items[x])))
            if 'yelp.com/biz/' in source_url:
                source_url = str(re.findall(pattern, str(list_items[x])))
                break
            else:
                continue

        source_url_final = source_url.replace("['q=", "").replace("&amp']", "")
        list_of_urls.append(source_url_final)
        list_of_names.append(test_term_final)

    except:
        source_url = "No URL Found"
        pass



    source_url_final = source_url.replace("['q=", "").replace("&amp']", "")
    print(source_url_final)



#make dank lists
    list_of_urls.append(source_url_final)
    list_of_names.append(test_term_final)


#create a dictionary with the name and url

dictionary = dict(zip(list_of_names, list_of_urls))


#export list of urls to csv file called "output.csv"  
#csvfile = "output.csv"
#with open(csvfile, "w") as output:
    #writer = csv.writer(output, lineterminator='\n')
    #for val in list_of_urls:
        #writer.writerow([val])  


#export dictionary to csv file
with open('names_with_url.csv','wb') as f:
    w = csv.writer(f)
    w.writerows(dictionary.items())

print("Done, son")
