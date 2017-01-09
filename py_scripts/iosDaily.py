#!/usr/bin/python

import urllib.request, urllib.error, urllib.parse
import json
import os
import shutil

opener = urllib.request.build_opener()
opener.addheaders = [('X-HockeyAppToken', 'cabe2331b360467abb0e6a5426600c94')]
data = json.load(opener.open('https://rink.hockeyapp.net/api/2/apps/cf2e7547bb4d59b718fe171e64ba5786/app_versions?include_build_urls=true'))

for build in data['app_versions']:
        if build['appsize'] != 0:
            downloadUrl = build['build_url']
            response = urllib.request.urlopen(downloadUrl).read()
            fnl = "/Users/amirwaisman/ofb.ipa"
            app = open(fnl, "wb")
            app.write(response)
            app.close

            version = build['version']
            print(version)
            break


