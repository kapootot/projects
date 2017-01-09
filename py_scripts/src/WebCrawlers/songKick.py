#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
import re

print('\n')


domain = "http://www.songkick.com/"
suffix = "&page="
suffix2 = "&utf8=%E2%9C%93#date-filter-form"

def set_dates():
    global min_month, min_day, min_year, max_month, max_day, max_year, domain, suffix, suffix2, base, min_date_str, max_date_str

    base = "http://www.songkick.com/metro_areas/28443-germany-berlin?filters%5B"

    min_date = raw_input("Start date? (mm/dd/yyyy)")
    max_date = raw_input("End date? (mm/dd/yyyy)")

    min_month = min_date[:2]
    min_day = min_date[3:5]
    min_year = min_date[6:]

    max_month = max_date[:2]
    max_day = max_date[3:5]
    max_year = max_date[6:]

    min_date_str = "minDate%5D="+min_month+"%2F"+min_day+"%2F"+min_year
    max_date_str = "&filters%5BmaxDate%5D="+max_month+"%2F"+max_day+"%2F"+max_year+"&filters%5B"
    base = base + min_date_str + max_date_str

def crawl_pages(max_page):
    for n in range(1, max_page+1):
        pageNum = n
        finalSuffix = suffix + str(pageNum) + suffix2
        url = base+finalSuffix

        html = requests.get(url).text
        # print "\nBrowsing to URL: " + url + "\n"

        soup = BeautifulSoup(html, 'html.parser')

        dates = []
        all_dates = []
        all_li = soup.find_all('li')

        for li in all_li:
            match = re.search(r"<li title", str(li))
            if match:
                all_dates.append(li)

        for date in all_dates:
            date = str(date)
            start_idx = date.find("\"")
            end_idx = date.find("\"", start_idx+1)
            dates.append(date[start_idx+1:end_idx])

        all_artists = soup.find_all('p', {'class': 'artists summary'})
        all_venues = soup.find_all('span', {'class': 'venue-name'})

        if not len(all_artists) < 1:
            for i in range(len(all_artists)):
                try:
                    artist = all_artists[i].contents[1].contents[1].contents[1].string

                    if "Scotch & Soda" in artist:
                        continue

                    href = all_artists[i].contents[1].get('href')
                    venue = all_venues[i].contents[0].string
                    date = dates[i]

                    print artist, " | ", date, " | ", venue, " | ", domain+href, "\n"

                except:
                    pass
        else:
            break

def run(max_pages):
    set_dates()
    crawl_pages(max_pages)

run(100)
