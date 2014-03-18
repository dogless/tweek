from django.shortcuts import render
from bs4 import BeautifulSoup
import urllib2
import json

# Create your views here.
def index(request):
	base = "https://api.twitch.tv/kraken"	
	req = urllib2.Request(base + "/videos/top")
	req.add_header('Accept', 'application/vnd.twitchtv.v2+json')
	opener = urllib2.build_opener()
	f = opener.open(req)
	jsonObject = json.load(f)
	video = jsonObject.get("videos")[0]
	soup = BeautifulSoup(video.get('embed', None))
	embedData = soup.find('param', attrs = {'name' : 'flashvars'})['value']
	context = {
			'video' : embedData
	}
	return render(request, 'tweek/index.html', context)

	
