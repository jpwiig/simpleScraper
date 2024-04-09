import os
import requests

def scraping(url):
    if len(url) == 0:  
        print('please use a valid lenght length')
    else: 
        print('lets scrape boys: TODAYS VICTIM IS: ' + url)
        
        req = requests.get(url)

        print(str(req))
        if req.ok: #TODO: add possibility to scrape images and pdfs
            print(req.text)