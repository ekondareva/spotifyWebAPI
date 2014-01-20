from django.conf.urls import patterns, include, url

from Spotify.views.musicViews import *


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SpotifyWebApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', home),
    url(r'^index/$', home),
    url(r'^albums/$', albums),
    url(r'^tracks/$', tracks),

    url(r'^searchartist/$', searchArtist),
    url(r'^searchalbum/$', searchAlbum),
    url(r'^searchtrack/$', searchTrack),
    url(r'^viewartist/$', viewArtist),
    url(r'^viewalbum/$', viewAlbum),
)