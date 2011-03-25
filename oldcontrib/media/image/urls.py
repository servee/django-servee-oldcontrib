from django.conf.urls.defaults import *

urlpatterns = patterns('oldcontrib.media.image.views',
    url(r'^upload_image/$', view='upload_image', name='upload_image'),
)