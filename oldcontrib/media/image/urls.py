from django.conf.urls.defaults import *
from django.conf.urls import patterns, url

urlpatterns = patterns('oldcontrib.media.image.views',
    url(r'^upload/$', view='upload_image', name='upload_image'),
    url(r'^recent/$', view='recent_photos', name='recent_photos'),
)