from django.conf.urls.defaults import *

urlpatterns = patterns('oldcontrib.media.document.views',
    url(r'^upload_document/$', view='upload_document', name='upload_document'),
)