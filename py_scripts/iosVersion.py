#!/usr/bin/python

import urllib.request, urllib.error, urllib.parse
import json

opener = urllib.request.build_opener()

opener.addheaders = [('X-HockeyAppToken', '8280a57c703d411697b4f05d5506f39c')]
data = json.load(opener.open('https://rink.hockeyapp.net/api/2/apps/cf2e7547bb4d59b718fe171e64ba5786/app_versions'))

for build in data['app_versions']:
        if build['appsize'] != 0:
                version = build['version'] 
                #version = int(version) + 1
                print(version)
                break


