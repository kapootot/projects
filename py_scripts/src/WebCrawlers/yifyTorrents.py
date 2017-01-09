#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
import rottenTomatoes

base = "https://yts.ag/browse-movies/0/all/all/7/latest"
suffix = "?page="

print('\n')

def crawl_pages(max_page):
    for n in range(1,max_page+1):
        if n < 2:
            url = base
        else:
            url = base+suffix+str(n)

        html = requests.get(url).text
        # print "Accessing: " + url

        soup = BeautifulSoup(html, 'html.parser')


        all_links = soup.find_all('a', {'class': 'browse-movie-title'})
        all_ratings = soup.find_all('h4', {'class': 'rating'})
        div_tags = soup.find_all('div', {'class': 'browse-movie-tags'})
        all_years = soup.find_all('div', {'class': 'browse-movie-year'})

        for i in range(len(all_links)):
            title = all_links[i].string
            rtScores = rottenTomatoes.getRtScores(title)
            year = all_years[i].string
            print title, "|", year, "|", "IMDB Score: " + all_ratings[i].string.split(" / 10")[0], "|", "RT Scores:", rtScores
            print div_tags[i].contents[1].get('href'), "\n"

crawl_pages(2)