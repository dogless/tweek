from django.shortcuts import render

import urllib2
import json

# Create your views here.
def index(request):
	base = "https://api.twitch.tv/kraken"	
	req = urllib2.Request(base + "/videos/top")
	req.add_header('Accept', 'application/vnd.twitchtv.v2+json')
	opener = urllib2.build_opener()
	f = opener.open(req)
	object = json.load(f)
	thing = object.get("videos")[0]
	embed = thing.get('embed')
	context = {
			'video' : embed
	}
	return render(request, 'tweek/index.html', context)

	
