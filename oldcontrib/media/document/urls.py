from django.conf.urls.defaults import *
from django.conf.urls import *

urlpatterns = patterns('oldcontrib.media.document.views',
    url(r'^upload/$', view='upload_document', name='upload_document'),
    url(r'^recent/$', view='recent_documents', name='recent_documents'),
)