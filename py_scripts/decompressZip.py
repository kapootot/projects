#!/usr/bin/python

import os
import gzip
import ntpath
import time

zipExts = [".gz"]
root = r"/Users/amirwaisman/Google Drive/"
dstPath = "/Users/amirwaisman/Movies/"

def checkIfZip(file):
    ext = os.path.splitext(file)[1]
    if ext in zipExts:
        return True
    else:
        return False

def decompressZip(zipFile):
    pathOftxt = ntpath.dirname(zipFile)
    char = os.path.splitext(ntpath.basename(zipFile))[0]
    txtFile = pathOftxt+"/"+char+".txt"

    outName = getOriginalName(txtFile)

    fullOutName = dstPath+outName

    print("\nDecompressing: " + zipFile)
    print("\nTo: " + fullOutName)

    inF = gzip.GzipFile(zipFile, 'rb')
    s = inF.read()
    inF.close()

    outF = file(fullOutName, 'wb')
    outF.write(s)
    outF.close()

    os.remove(txtFile)
    os.remove(zipFile)

def getOriginalName(txtFile):
    f = open(txtFile, "r")
    name = f.readline()
    f.close()
    name = name[:-2]

    return name

def walk(rootdir):
    for root, dirs, files in os.walk(rootdir):
        for file in files:
            fname = os.path.join(root, file)
            if checkIfZip(file):
                decompressZip(fname)

start = time.time()

walk(root)

print("\nTime: "+ str(time.time() - start) + " seconds")