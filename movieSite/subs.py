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

server_url = 'http://api.opensubtitles.org/xml-rpc'
server = xmlrpclib.Server(server_url)
user = 'waamir'
password = 'lihofet'
videoExtensions = [".avi",".mp4",".mkv",".mpg",".mpeg",".mov",".rm",".vob",".wmv",".flv",".3gp"]
login_info = server.LogIn('', '', 'eng', 'WaismanSub')
print login_info
token = login_info.values()[2]
#log = open('D:\\log.txt', 'w')

#hash method SubDB
def get_hash(name):
        readsize = 64 * 1024
        with open(name, 'rb') as f:
            data = f.read(readsize)
            f.seek(-readsize, os.SEEK_END)
            data += f.read(readsize)
        return hashlib.md5(data).hexdigest()


#hash method OpenSubtitles
def hashFile(name): 

      try: 
                 
                longlongformat = '<q'  # little-endian long long
                bytesize = struct.calcsize(longlongformat) 
                    
                f = open(name, "rb") 
                    
                filesize = os.path.getsize(name) 
                hash = filesize 
                    
                if filesize < 65536 * 2: 
                       return "SizeError" 
                 
                for x in range(65536/bytesize): 
                        buffer = f.read(bytesize) 
                        (l_value,)= struct.unpack(longlongformat, buffer)  
                        hash += l_value 
                        hash = hash & 0xFFFFFFFFFFFFFFFF #to remain as 64bit number  
                         
    
                f.seek(max(0,filesize-65536),0) 
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

#method for downloading movie subs - SubDB

def subdb(file):
    try:
        hash = get_hash(file)           
        headers = { 'User-Agent' : 'SubDB/1.0 (subtitle-downloader/1.0; http://github.com/manojmj92/subtitle-downloader)' }
        url = "http://api.thesubdb.com/?action=download&hash=" + hash + "&language=en"
        req = urllib2.Request(url, '', headers)
        response = urllib2.urlopen(req).read()
        fnl = os.path.splitext(file)[0] + ".srt"
        sub = open(fnl, "wb")
        sub.write(response)
        sub.close
        #log.write("Downloaded Subtitles from SubDB for: " + file + '/n')
        print "Subtitle successfully Downloaded (SubDB) for file " + file
    except:
        print "...."
        
    
    
#method for downloading movie subs
def sub_download(file):
    try:
        if os.path.exists(os.path.splitext(file)[0] + ".srt"):
            print "Subtitles already exists for: " + file
            #log.write("Subtitles already exists for: " + file + '\n')
        else:
            file_size = os.path.getsize(file)
            movie = [{'sublanguageid': 'eng', 'moviehash': hashFile(file), 'moviebytesize': str(file_size)}]
            subfile = server.SearchSubtitles(token, movie)
            if subfile.get('data', "None") == False:
                print "No Subtitles found for:" + file
                #log.write("No Subtitles found for:" + file + ". Trying with SubDB" "\n")
                subdb(file)
            else:
                sublink = [subfile.get('data', "None")[0].get('SubDownloadLink', 'None')]
                #log.write(str(sublink))
                #response = server.DownloadSubtitles(token, subid)
                #response = requests.get(sublink[0])
                req = urllib2.Request(sublink[0])
                response = urllib2.urlopen(req).read()
                unzipped = zlib.decompress(response, 47)
                fnl = os.path.splitext(file)[0] + ".srt"
                sub = open(fnl, "wb")
                sub.write(unzipped)
                sub.close
                #log.write("Downloaded Subtitles for: " + file + '/n')
                print "Downloaded Subtitles for: " + file
    except:
        print "Problem with Download :("
        return

        

#method for verifying that the file is video
def checkVideoExt(file):
    ext = os.path.splitext(file)[1]
    if ext in videoExtensions:
        return True
    else:
        return False

#main method for os.walk
def walk(rootdir):
    for root, dirs, files in os.walk(rootdir):
        for file in files:
            if checkVideoExt(file):
                fname = os.path.join(root, file)
                sub_download(fname)
                
                
root = "/run/user/1000/gvfs/smb-share:server=studio,share=completed"

if __name__ =='__main__':
    walk(root)      
#log.close()

#logout
print server.LogOut(token)
