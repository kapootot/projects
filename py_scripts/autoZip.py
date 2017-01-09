#!/usr/bin/python

import xmlrpc.client
import struct
import os
import gzip
import shutil
import string
import random
import time
import ntpath


base = r"C:\Users\kapootot\Google Drive\\"
server_url = 'http://api.opensubtitles.org/xml-rpc'
server = xmlrpc.client.Server(server_url)
user = 'waamir'
password = 'lihofet'
videoExtensions = [".avi", ".mp4", ".mkv", ".mpg", ".mpeg", ".mov", ".rm", ".vob", ".wmv", ".flv", ".3gp"]
login_info = server.LogIn(user, password, 'eng', 'WaismanSub')
# print login_info
token = list(login_info.values())[2]


def checkItem(movie):
    f = open("C:\Torres\Completed\list.txt", "r")
    movies = f.readlines()
    f.close()

    found = False

    for line in movies:
        if movie in line:
            found = True
            return found
    if not found:
        f = open("C:\Torres\Completed\list.txt", "a")
        f.write(movie+"\n")
        f.close()
        print("\nAdded: "+movie)
        return False

def checkVideoExt(file):
    ext = os.path.splitext(file)[1]
    if ext in videoExtensions:
        return True
    else:
        return False

def scanForNewMovie(file):
    try:
        file_size = os.path.getsize(file)
        movie = [{'sublanguageid': 'eng', 'moviehash': hashFile(file), 'moviebytesize': str(file_size)}]
        subfile = server.SearchSubtitles(token, movie)
        if not subfile.get('data', "None"):
            return
        else:
            movname = [subfile.get('data', "None")[0].get('MovieName', 'None')]
            movname = movname[0]

            if not checkItem(movname):
                zipFile(file)

    except Exception as e:
        print(str(e))
        # return

def zipFile(movFile):
    randChar = random.choice(string.letters)

    f = open(base + randChar + ".txt", 'a')
    f.write(ntpath.basename(movFile)+'\n')
    f.close()

    while os.path.isfile(base+randChar+ '.gz'):
        randChar = random.choice(string.letters)

    # ext = os.path.splitext(movFile)[1]
    gzipFile = base + randChar + '.gz'

    with open(movFile, 'rb') as f_in, gzip.open(gzipFile, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

    os.remove(movFile)


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

def walk(rootdir):
    for root, dirs, files in os.walk(rootdir):
        for file in files:
            fname = os.path.join(root, file)
            if checkVideoExt(file):
                scanForNewMovie(fname)

root = "C:\Torres\Completed"

start = time.clock()

walk(root)

print("\nTime: "+ str(time.clock() - start) + " seconds")