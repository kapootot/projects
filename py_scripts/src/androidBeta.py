#!/usr/bin/python

import urllib.request, urllib.error, urllib.parse
import json
import os
import shutil

opener = urllib.request.build_opener()
opener.addheaders = [('X-HockeyAppToken', 'cabe2331b360467abb0e6a5426600c94')]
data = json.load(opener.open('https://rink.hockeyapp.net/api/2/apps/67b3b38d645c6890cdd9a008af43a676/app_versions?include_build_urls=true'))

downloadUrl = data['app_versions'][0]['build_url']

version = data['app_versions'][0]['version']
version = int(version[-3:])
print("Downloading version: "+ str(version))

response = urllib.request.urlopen(downloadUrl).read()
fnl = "/Users/amirwaisman/daily.apk"
apk = open(fnl, "wb")
apk.write(response)
apk.close

print("Done.")



