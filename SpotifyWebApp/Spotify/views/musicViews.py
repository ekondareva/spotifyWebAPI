__author__ = 'ekondareva'

import httplib2
import collections
import json

from django.utils.http import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect,HttpRequest,\
    HttpResponseNotFound, Http404, HttpResponseNotAllowed,HttpResponseForbidden

from Spotify.ViewModels.Album import *
from Spotify.ViewModels.Artist import *
from Spotify.ViewModels.Track import *

def home(request):
    return render_to_response('index.html',
        context_instance = RequestContext(request))

def albums(request):
    return render_to_response('albums.html',
        context_instance = RequestContext(request))

def tracks(request):
    return render_to_response('tracks.html',
        context_instance = RequestContext(request))


def searchArtist(request):
    if request.method == "POST" and 'searchvalue' in request.POST:
        artists = []
        if request.POST["searchvalue"].strip() != "":
            spfStr = "http://ws.spotify.com/search/1/artist.json?q=" + \
                     urlquote((request.POST["searchvalue"].strip()).encode("utf8"))
            conn = httplib2.Http()

            spfResponse, spfContent = conn.request(spfStr, "GET")

            if spfResponse.status == 200:
                data = json.loads(spfContent, object_pairs_hook = collections.OrderedDict)
                artists = []
                spfValues = data['artists']

                for v in spfValues:
                    artist = Artist(v['href'], v['name'], v['popularity'])
                    artists.append(artist)

        return render_to_response('index.html',
            {'artists': artists
            },
            context_instance = RequestContext(request))
    else:
        return HttpResponseRedirect('/')


def searchAlbum(request):
    if request.method == "POST" and 'searchvalue' in request.POST:
        albums = []
        if request.POST["searchvalue"].strip() != "":
            spfStr = "http://ws.spotify.com/search/1/album.json?q="\
                     + urlquote((request.POST["searchvalue"].strip()).encode("utf8"))
            conn = httplib2.Http()

            spfResponse, spfContent=conn.request(spfStr, "GET")

            if spfResponse.status == 200:
                data=json.loads(spfContent,object_pairs_hook=collections.OrderedDict)
                albums=[]
                spfValues=data['albums']

                for v in spfValues:
                    album=Album(v['name'],v['popularity'],v['href'],v['artists'][0]['name'])
                    albums.append(album)

        return render_to_response('albums.html',
            {'albums':albums
            },
            context_instance = RequestContext(request))
    else:
        return HttpResponseRedirect('/')

def searchTrack(request):
    if request.method == "POST" and 'searchvalue' in request.POST:
        tracks = []

        if request.POST["searchvalue"].strip() != "":
            spfStr = "http://ws.spotify.com/search/1/track.json?q=" + \
                     urlquote((request.POST["searchvalue"].strip()).encode("utf8"))
            conn = httplib2.Http()

            spfResponse, spfContent = conn.request(spfStr, "GET")

            if spfResponse.status == 200:
                data = json.loads(spfContent,object_pairs_hook=collections.OrderedDict)
                tracks = []
                spfValues = data['tracks']

                for v in spfValues:
                    track = Track(v['name'], v['popularity'], v['artists'][0]['name'], v['album']['name'], v['length'])
                    tracks.append(track)

        return render_to_response('tracks.html',
            {'tracks': tracks
            },
            context_instance = RequestContext(request))
    else:
        return HttpResponseRedirect('/')

def viewArtist(request):
    return render_to_response('index.html',
        context_instance = RequestContext(request))

def viewAlbum(request):
    return render_to_response('index.html',
        context_instance = RequestContext(request))