#!/usr/bin/python

from bs4 import BeautifulSoup
import requests

base = "https://www.rottentomatoes.com/m/"

def getRtScores(movie_title):

    if movie_title[:3] == "the":
        movie_title = movie_title.split("the ")[1]

    movie_search_term = movie_title.replace("'", "")
    movie_search_term = movie_search_term.replace(" ", "_")
    url = base + movie_search_term
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    critic = soup.find('span', {'class': 'meter-value superPageFontColor'})
    audience = soup.find('div', {'class': 'audience-score meter'})
    try:
        critic_score = critic.text[:1] + "." + critic.text[1:-1]
        audience = audience.contents[1].contents[0].contents[3].contents[1].text
        audience_score = audience[1] + "." + audience[2:-2]

        avg_score = str(((float(critic_score) + float(audience_score)) / 2))

        return ["Critics: "+str(critic_score), "Audience: "+ str(audience_score), "Average: " + avg_score]

    except:
        try:
            movie_search_term = movie_title.replace("'", "")
            movie_search_term = movie_search_term.replace(" ", "-")
            url = base + movie_search_term
            html = requests.get(url).text
            soup = BeautifulSoup(html, 'html.parser')

            critic = soup.find('span', {'class': 'meter-value superPageFontColor'})
            audience = soup.find('div', {'class': 'audience-score meter'})

            critic_score = critic.text[:1] + "." + critic.text[1:-1]
            audience = audience.contents[1].contents[0].contents[3].contents[1].text
            audience_score = audience[1] + "." + audience[2:-2]

            avg_score = str(((float(critic_score) + float(audience_score)) / 2))

            # print "\nTomatometer: " + critic_score
            # print "Audience score: " + audience_score
            #
            # print "\nCalculated score: " + avg_score

            return ["Critics: "+str(critic_score), "Audience: "+ str(audience_score), "Average: " + avg_score]
        except:
            pass


    if __name__ == '__main__':
        print getRtScores("abyss")