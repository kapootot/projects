#!/usr/bin/python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import string
import itertools

pageNum = 1
lines = []
moviesunsorted = []
movies = []


def createSoup(page):
    url = 'http://sceper.ws/category/movies/page/'+str(page)
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def checkTitle(soup):
    title = soup.title.text
    if not ("Movies Archive | Sceper" in title):
        print("Actual title: " + title)
        exit("BAD WEB PAGE")

def getMovieDetails(mov, detail):

    # 0 - title, 1 - date, 2 - genre, 3 - imdb , 4 - rt, 5 - director

    if detail == "title":
        return mov[0]
    elif detail == "date":
        return mov[1][1]
    elif detail == "genre":
        return mov[2]
    elif detail == "imdb":
        return mov[3][0]
    elif detail == "rt":
        return mov[4]
    elif detail == "director":
        return mov[5]
    else:
        return False

def getMovieList(soup):
    i = 0

    for x in soup.find_all("p"):
        moviesunsorted.append(x.get_text())

    for mo in moviesunsorted:
        if "Release Name:" in mo:
            movies.append(mo)

    for movie in movies:
        lines.append([])

        for line in string.split(movie, '\n'):
            line = line.encode('utf-8').strip()
            if ("Release Name:" in line) or ("Release Date:" in line)  or ("Directed By:" in line) or ("Genre" in line) or ("IMDB" in line) or ("RT" in line):
                if "Release Name:" in line:
                    s = string.split(line, "Release Name: ")[1]
                    rls_name = s

                    lines[i].append(rls_name)
                elif "Release Date:" in line:
                    s = string.split(line, "Release Date: ")
                    rls_date = s
                    lines[i].append(rls_date)
                elif "Directed By:" in line:
                    s = string.split(line, "Directed By: ")[1]
                    director = s
                    lines[i].append(director)
                elif "Genre" in line:
                    s = string.split(line, "Genre: ")[1]
                    genre = s
                    lines[i].append(genre)
                elif "IMDB" in line:
                    s = string.split(string.split(line, "IMDB Rating:")[1][1:4], " ")
                    imdb = s
                    lines[i].append(imdb)
                elif "RT" in line:
                    try:
                        s = string.split(line, "RT Critics: ")[1][0:3]
                    except:
                        s = string.split(line, "RT Critics: ")[0]
                    rt = s
                    lines[i].append(rt)

        i += 1

    return lines
'''
def removeDuplicates(movList):
    fnlList = []
    firstMov = True

    for mov in movList:
        if (firstMov):
            print "First"
            fnlList.append(mov)
            firstMov = False
        for m in fnlList:
            if not (mov[0][0:3] == m[0][0]):
                fnlList.append(mov)

    for x in fnlList:
        print x

'''
'''
def removeDuplicates(movList):
    fnlList = []
    firstMov = True
    currentFnl = fnlList
    for mov in movList:
        if (firstMov):
            #print "First"
            fnlList.append(mov)
            print "Adding: " + mov[0]
            firstMov = False
        else:
            currentFnl = fnlList
            for movInFnl in fnlList:

                movName = string.split(mov[0], ".")[0]
                movName2 = string.split(mov[0], ".")[1]
                fnlName = string.split(movInFnl[0], ".")[0]
                fnlName2 = string.split(movInFnl[0], ".")[1]

                if not ((movName in fnlName) and (movName2 in fnlName2)):
                    print movName
                    print movName2
                    print fnlName
                    print fnlName2
                    print "Adding: " + mov[0]
                    currentFnl.append(mov)
                    break'''

def removeDuplicates(movs):
    b = movs
    c = []
    i = 0

    first = True

    for mov in movs:
        print("Movie: "+str(mov))
        if first:
            c.append(mov)
            b.remove(mov)
            print("\n")
            first = False
            i += 1
            continue
        if not (mov[0][:5] == b[i][0][0:5]):
            c.append(mov)
            b.remove(mov)
            print("\n")
            i += 1
            continue



    return c
    '''for x in movs:
        print x
    print len(movs)

    print "\n\n"

    for x in c:
       print x
    print len(c)'''


soup = createSoup(4)
checkTitle(soup)
movs = getMovieList(soup)

for mov in movs:
    print(mov)

movs = removeDuplicates(movs)

for mov in movs:
    print(mov)


#movies = removeDuplicates(movs)
#for movie in movies:
 #   print movie



#for v in fnl:
    #print v

#print len(fnl)

#print removeDuplicates(fnl)








#testMov = movs[2]


# 0 - title, 1 - date, 2 - genre, 3 - imdb , 4 - rt, 5 - director
'''
print getMovieDetails(testMov,"title")
print getMovieDetails(testMov,"date")
print getMovieDetails(testMov,"genre")
print getMovieDetails(testMov,"imdb")
print getMovieDetails(testMov,"rt")
print getMovieDetails(testMov,"director")
'''
