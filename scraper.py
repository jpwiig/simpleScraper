import os
import requests
from urllib.parse import urlparse

def urlparser(url): #Parses a url as a name #TODO some kind of regexp to decide the  name of  the website itself
    urlParsed=urlparse(url)
    if urlParsed.netloc:
        return urlParsed.netloc
    else:
        return "error mitch"

def scraping(url):
    if len(url) == 0:  
        print('please use a valid lenght length')
    else: 
        print('lets scrape boys: TODAYS VICTIM IS: ' + url)
        urlString=str(url)
        req = requests.get(url)
# TODO: fix special character input from scraper
        print(str(req))
        if req.ok: #TODO: add possibility to scrape images and pdfs
            print('scraping ok! Do you want to save it as a file')
            ans = input().lower()
            print("ans: " + str(ans))
            if ans == 'ja' or ans == 'yes': 
                #save to file 
                print('saving to file')
                websitename=urlparser(url)
                filename=f'{websitename}.html'
                with open(filename, 'w') as datafile: 
                    datafile.write(str(req.text))
                exit
            else: 
                print('Terminal output')
                print(req.text)
