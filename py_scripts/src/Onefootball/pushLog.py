#!/usr/bin/python

import json
import urllib.request, urllib.error, urllib.parse

searchUrl = "https://papertrailapp.com/api/v1/events/search.json?id='10231264'"
opener = urllib.request.build_opener()
opener.addheaders = [('X-Papertrail-Token', 'Ru878RqgxHqearaHrlRK')]

data = json.load(opener.open(searchUrl))

print(data['events'][0])