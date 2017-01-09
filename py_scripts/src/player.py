#########################
# 06/2016				#
#						#
# @author: Amir Waisman #
#########################

#!/usr/bin/python

import urllib.request, urllib.error, urllib.parse
import json
import os
import shutil

opener = urllib.request.build_opener()
data = json.load(opener.open('http://vintagemonster.onefootball.com/api/player/en/36.json'))

print(data)

