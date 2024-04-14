#! /bin/python3
import scraper as s
import sys

#this is where we will test the web scraper
print('awsome web scraper')
if not sys.argv[1]:
    input = (str(input('please write your url')))
    s.scraping(input)
else: 
    s.scraping(sys.argv[1])