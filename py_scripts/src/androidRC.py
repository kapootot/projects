#!/usr/bin/python

import urllib.request, urllib.error, urllib.parse
import json
import os
import shutil

opener = urllib.request.build_opener()
opener.addheaders = [('X-HockeyAppToken', 'cabe2331b360467abb0e6a5426600c94')]
data = json.load(opener.open('https://rink.hockeyapp.net/api/2/apps/1ec10c5c654d4c1ba3e40149ca3d0a3a/app_versions?include_build_urls=true'))

for version in data['app_versions']:
    if(version['appsize'] != 0):
        downloadUrl = version['build_url']
        version = version['version']
        version = int(version[-3:])
        break

print("Downloading version: "+ str(version))

response = urllib.request.urlopen(downloadUrl).read()
fnl = "/Users/amirwaisman/daily.apk"
apk = open(fnl, "wb")
apk.write(response)
apk.close

print("Done.")


