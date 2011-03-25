from django.conf.urls.defaults import *

urlpatterns = patterns('oldcontrib.media.video.views',
    url(r'^upload_video/$', view='upload_video', name='upload_video'),
)