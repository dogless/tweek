from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import random 
import urllib2
import json

# Create your views here.
def index(request):
	embedData = grabVideo()
	context = {
			'video' : embedData
	}
	return render(request, 'tweek/index.html', context)

def next(request):
	results = {'success':'False'}
	embedData = grabVideo()
	results['embed'] = embedData
	results['success'] = 'True'
	jason = json.dumps(results)
	return HttpResponse(jason, content_type='application/json')

def grabVideo(number=-1):
	base = "https://api.twitch.tv/kraken"	
	req = urllib2.Request(base + "/videos/top")
	req.add_header('Accept', 'application/vnd.twitchtv.v2+json')
	opener = urllib2.build_opener()
	f = opener.open(req)
	jsonObject = json.load(f)
	topVideos = jsonObject.get("videos", None)
	whichVid =  random.randint(0, len(topVideos)-1) if (number == -1) else number
	video = topVideos[whichVid]
	soup = BeautifulSoup(video.get('embed', None))
	embedData = soup.find('param', attrs = {'name' : 'flashvars'})['value']
	return embedData