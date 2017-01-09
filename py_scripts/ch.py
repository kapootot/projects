#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
import csv

url = 'https://rarbg.to/torrents.php?category=movies'

response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')

print(soup.title)

#print soup.prettify()