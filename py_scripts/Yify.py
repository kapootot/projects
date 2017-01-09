import re
import sys
from zipfile import ZipFile
import os

import requests
from html2text import HTML2Text

BASE_URL = 'http://www.yifysubtitles.com'


def get(url):
    '''Retrieve page content and use html2text to convert into readable text.'''
    # get webpage content for this url
    r = requests.get(url)
    # raise exception if status code is not 200
    r.raise_for_status()

    # use html2text to transfer html to readable text
    h = HTML2Text()
    h.ignore_links = False
    text = h.handle(r.text)

    return text


def search_subtitle(query):
    '''Search subtitle by query in parameter.'''
    text = get('{}/search?q={}'.format(BASE_URL, query))

    # try to find subtitle link in this page
    m = re.search(r'(\/movie-imdb\/.+)\)', text)
    if m:
        # call get_subtitles() to get all available subtitles
        get_subtitles('{}{}'.format(BASE_URL, m.group(1)))


def get_subtitles(url):
    '''Find all subtitles url for the movie.'''
    # get webpage content for this url
    text = get(url)

    # save english subtitles
    subs = []

    for line in text.splitlines():
        # find upvote count, subtitle language and subtitle link
        m = re.search(r'upvote(\d+).+\[(\w+) subtitle.*\((.*?)\)', line)
        if not m:
            continue

        upvote, language, link = m.group(1), m.group(2), m.group(3)
        # we only want english subtitle
        if language == 'English':
            subs.append({
                'up': upvote,
                'link': link
            })
    # sort list by upvote count
    subs.sort(key=lambda x: int(x['up']), reverse=True)

    # only download subtitle which has the most upvote count
    get_subtitle(subs[0]['link'])


def get_subtitle(url):
    '''Download the specific subtitle.'''
    text = get('{}{}'.format(BASE_URL, url))

    m = re.search(r'\[Download subtitle\]\((.*\n.*)\)', text)
    if m:
        # remove all newline
        link = m.group(1).replace('\n', '')
        print(('Download {}'.format(link)))

        # use last part of url as file name
        filename = link.split('/')[-1]

        # save the file to current directory
        with open(filename, 'wb') as f:
            f.write(requests.get(link).content)

        # extract subtitles from zip file
        with ZipFile(filename) as zf:
            zf.extractall()

        # after extracting subtitles, remove zip file
        os.remove(filename)

def main():
    try:
        #search_subtitle(sys.argv[1])
        search_subtitle("Winter on Fire")
    except IndexError:
        sys.exit('Usage: yify <movie>')

if __name__ == '__main__':
    main();