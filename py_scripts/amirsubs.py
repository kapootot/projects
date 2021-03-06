########
# 03/2015
#
# @author: Amir Waisman
########

import xmlrpclib
import struct
import zlib
import urllib2
import hashlib
import os
import regex

server_url = 'http://api.opensubtitles.org/xml-rpc'
server = xmlrpclib.Server(server_url)
user = 'waamir'
password = 'lihofet'
videoExtensions = [".avi", ".mp4", ".mkv", ".mpg", ".mpeg", ".mov", ".rm", ".vob", ".wmv", ".flv", ".3gp"]
login_info = server.LogIn(user, password, 'eng', 'WaismanSub')
print login_info
token = login_info.values()[2]


# log = open('D:\\log.txt', 'w')

# hash method SubDB
def get_hash(name):
    readsize = 64 * 1024
    with open(name, 'rb') as f:
        data = f.read(readsize)
        f.seek(-readsize, os.SEEK_END)
        data += f.read(readsize)
    return hashlib.md5(data).hexdigest()


# hash method OpenSubtitles
def hashFile(name):
    try:

        longlongformat = '<q'  # little-endian long long
        bytesize = struct.calcsize(longlongformat)

        f = open(name, "rb")

        filesize = os.path.getsize(name)
        hash = filesize

        if filesize < 65536 * 2:
            return "SizeError"

        for x in range(65536 / bytesize):
            buffer = f.read(bytesize)
            (l_value,) = struct.unpack(longlongformat, buffer)
            hash += l_value
            hash = hash & 0xFFFFFFFFFFFFFFFF  # to remain as 64bit number

        f.seek(max(0, filesize - 65536), 0)
        for x in range(65536 / bytesize):
            buffer = f.read(bytesize)
            (l_value,) = struct.unpack(longlongformat, buffer)
            hash += l_value
            hash = hash & 0xFFFFFFFFFFFFFFFF

        f.close()
        returnedhash = "%016x" % hash
        return returnedhash

    except(IOError):
        return "IOError"


# method for downloading movie subs - SubDB
def subdb(file):
    try:
        hash = get_hash(file)
        headers = {'User-Agent': 'SubDB/1.0 (subtitle-downloader/1.0; http://github.com/manojmj92/subtitle-downloader)'}
        url = "http://api.thesubdb.com/?action=download&hash=" + hash + "&language=en"
        req = urllib2.Request(url, '', headers)
        response = urllib2.urlopen(req).read()
        fnl = os.path.splitext(file)[0] + ".srt"
        sub = open(fnl, "wb")
        sub.write(response)
        sub.close
        print "Subtitle successfully Downloaded (SubDB) for file " + file
    except:
        path = file.__str__()
        #path = "D:\Bittorrent\Completed\Movies_and_TV_Shows\BBC.Amy.Winehouse.In.Her.Own.Words.720p.WEBRip.x264.AAC.MVGroup.org.mp4"
        fileName = regex.getFileName(path)
        print fileName
        moviename = regex.getMovName(fileName)
        print ("Trying Yify Subs with: "+moviename)
        try:
            Yify.search_subtitle(moviename)
        except:
            return

def rename(fname, file):
    newext = ".srt"
    if not os.path.splitext(file)[1:] == (".srt"):
        print "Renamed: " + fname
        root, ext = os.path.splitext(fname)
        print root
        os.rename(fname, root+newext)

# method for downloading movie subs
def sub_download(file):
    try:
        if os.path.exists(os.path.splitext(file)[0] + ".srt"):
            return
        else:
            file_size = os.path.getsize(file)
            movie = [{'sublanguageid': 'eng', 'moviehash': hashFile(file), 'moviebytesize': str(file_size)}]
            subfile = server.SearchSubtitles(token, movie)
            if subfile.get('data', "None") == False:
                # print "No Subtitles found for:" + file
                # log.write("No Subtitles found for:" + file + ". Trying with SubDB" "\n")
                subdb(file)
            else:
                sublink = [subfile.get('data', "None")[0].get('SubDownloadLink', 'None')]
                movname = [subfile.get('data', "None")[0].get('MovieName', 'None')]
                req = urllib2.Request(sublink[0])
                response = urllib2.urlopen(req).read()
                unzipped = zlib.decompress(response, 47)
                fnl = os.path.splitext(file)[0] + ".srt"
                sub = open(fnl, "wb")
                sub.write(unzipped)
                sub.close
                print "Downloaded Subtitles for: " + movname[0]
    except:
        # print "Problem with Download :("
        #subdb(file)
        return


# method for verifying that the file is video
def checkVideoExt(file):
    ext = os.path.splitext(file)[1]
    if ext in videoExtensions:
        return True
    else:
        return False


# main method for os.walk
def walk(rootdir):
    for root, dirs, files in os.walk(rootdir):
        for file in files:
            fname = os.path.join(root, file)
            #rename(fname, file)
            if checkVideoExt(file):
                sub_download(fname)


root = "/Users/amirwaisman/Movies"

walk(root)


# logout
print server.LogOut(token)