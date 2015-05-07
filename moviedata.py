#!/usr/bin/python

########
# @author: Amir Waisman
########

import os
import xmlrpclib
import struct
import zlib
import requests
import urllib2
import hashlib
import sys
import ast
import time

server_url = 'http://api.opensubtitles.org/xml-rpc'
server = xmlrpclib.Server(server_url)
user = 'waamir'
password = 'lihofet'
videoExtensions = [".avi",".mp4",".mkv",".mpg",".mpeg",".mov",".rm",".vob",".wmv",".flv",".3gp"]
login_info = server.LogIn('', '', 'eng', 'WaismanSub')
print login_info
token = login_info.values()[2]
#log = open('D:\\log.txt', 'w')

#hash method OpenSubtitles


def hashFile(name): 

      try: 
                 
                longlongformat = '<q'  # little-endian long long
                bytesize = struct.calcsize(longlongformat) 
                    
                f = open(name, "rb") 
                    
                moviesize = os.path.getsize(name) 
                hash = moviesize 
                    
                if moviesize < 65536 * 2: 
                       return "SizeError" 
                 
                for x in range(65536/bytesize): 
                        buffer = f.read(bytesize) 
                        (l_value,)= struct.unpack(longlongformat, buffer)  
                        hash += l_value 
                        hash = hash & 0xFFFFFFFFFFFFFFFF #to remain as 64bit number  
                         
    
                f.seek(max(0,moviesize-65536),0) 
                for x in range(65536/bytesize): 
                        buffer = f.read(bytesize) 
                        (l_value,)= struct.unpack(longlongformat, buffer)  
                        hash += l_value 
                        hash = hash & 0xFFFFFFFFFFFFFFFF 
                 
                f.close() 
                returnedhash =  "%016x" % hash 
                return returnedhash 
    
      except(IOError): 
                return "IOError"

    
#method for fetching movie data

def dataFetch(movie):
    try:
        movie_size = os.path.getsize(movie)
        movie = [{'sublanguageid': 'eng', 'moviehash': hashFile(movie), 'moviebytesize': str(movie_size)}]
        submovie = server.SearchSubtitles(token, movie)
        _submovie = submovie
        if submovie.get('data', "None") == False:
            #print "Not found"
            return 
        else:
            _moviedata = [submovie.get('data', "None")[0].get("MovieName", "None"), submovie.get('data', "None")[0].get("MovieYear", "None"), submovie.get('data', "None")[0].get("IDMovieImdb", "None")]
 #           print _moviedata    
            return _moviedata
    except:
        
        return

                
                
root = "D:\\Utorrent\Completed\\"

tstFile = "D:\\Utorrent\Completed\\The Thin Blue Line (1988) [1080p]\\The.Thin.Blue.Line.1988.1080p.BluRay.x264.YIFY.mp4"

def getDownLoaded(movie):
    
    date = time.ctime(os.path.getctime(movie))
    return date

def setid(idnum):
    if len(idnum) == 5:
       fnlid = "tt00"+idnum
       return fnlid 
    elif len(idnum) == 6:
        fnlid = "tt0"+idnum
        return fnlid
    else:
         fnlid = "tt"+idnum
         return fnlid

def getImdbRating(id):

    url = "http://www.omdbapi.com/?i=" + id
    #print url
    req = urllib2.Request(url)
    response = urllib2.urlopen(req).read()
    dbdict = ast.literal_eval(response)
    rating = dbdict.get("imdbRating", "None")
    return rating
    
def subsExist(movie):
    if os.path.exists(os.path.splitext(movie)[0] + ".srt"):
        return "Y"
    else:
        return "N"
    

def Main(movie):
    data = dataFetch(movie)
    subsExist(movie)
    _moviedata = [data[0]] + [data[1]] + [getImdbRating(setid(data[2]))] + [subsExist(movie)] + [getDownLoaded(movie)]
    #print _moviedata
    #print server.LogOut(token)
     
    return _moviedata
    server.LogOut(token)

if __name__=="__main__":
    Main(tstFile)
