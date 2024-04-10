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
            print('scraping ok! Do you want to save it as a file')
            ans = str(input())
            if ans.lower == 'ja' or ans.lower == 'yes': 
                #save to file 
                print('saving to file')
            elif ans.lower == 'no' or ans.lower == 'nei' : 
                print('Terminal output')
                print(req.text)