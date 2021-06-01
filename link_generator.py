#This code helps us to scrape links and append them to a list so that we can use that list to scrape movie names in the
#movie_names_scraper.py and then use it for our hangman game
 
import requests
from bs4 import BeautifulSoup
import urllib.request
import re
import pandas as pd
 
parser = 'html.parser'
resp = urllib.request.urlopen("https://en.wikipedia.org/wiki/Lists_of_Bollywood_films")
soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))
links_list = []
 
for link in soup.find_all('a', href=True):
    links_list.append(link['href'])
 
#print(links_list)
 
str_list= []
final_list= []
for l in links_list:
    str_list.append(str(l))
needle = '/wiki/'
 
for urls in str_list:
    if(urls.lower().startswith(needle)):
        if('help' in urls or ":" in urls):
            continue
        elif(urls.startswith('/wiki/List_of_Bollywood_films_of')):
            final_list.append(urls)
 
#print(final_list)
 
#now we will append these hyperlinks to original link that we used to access these links and then we will use the complete links list
#to access the links and then extract the data from the tables into a file which we will use for our hangman project
 
list_of_links = [] #this is our list of complete links that we require for extracting individual table from each link
for u in final_list:
    list_of_links.append('https://en.wikipedia.org/wiki' + (u.replace("/wiki","")))
#print (list_of_links)
 
#This is the part where we extract Titles from the the wikipedia pages now:
movie_names = []
list_of_dfs = [] #list of dataframes, since each year has a different table shape
 
for ls in list_of_links:
    table_class="wikitable sortable jquery-tablesorter"
    response=requests.get(ls)
    s = BeautifulSoup(response.text, 'html.parser')
    temp = s.find('table',{'class':"wikitable"})
    df=pd.read_html(str(temp))
    df=pd.DataFrame(df[0],index= None)
    list_of_dfs.append(df)
 
#print(list_of_dfs)
 
movie_names = []
#from individual dataframes extract titles
 
for ds in list_of_dfs:
    if('Title' in ds.columns):
        movie_names.append(ds['Title'])
 
#print(movie_names)
 
textfile = open("movie_names.txt", "w")
for element in movie_names:
    textfile.write(str(element) + "\n")
textfile.close()
 