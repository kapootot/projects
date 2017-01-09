#!/usr/bin/python

import urllib.request, urllib.error, urllib.parse
import json
import os
import shutil

opener = urllib.request.build_opener()
opener.addheaders = [('X-HockeyAppToken', 'cabe2331b360467abb0e6a5426600c94')]
data = json.load(opener.open('https://rink.hockeyapp.net/api/2/apps/e880248b1f9af399930368198c4811c7/app_versions?include_build_urls=true'))

versions = data['app_versions']

i = 0

for ver in versions:
	i += 1
	print("************  Version no.: "+str(i) + "*************"+"\n")
	print(ver['created_at'])
	print("Version: " + ver['version'][-3:])

