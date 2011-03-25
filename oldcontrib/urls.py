from django.conf.urls.defaults import *

urlpatterns = patterns("",
    # servee provided
    (r"^tools/gallery/", include('oldcontrib.tools.gallery.urls')),
    (r"^media/docs/", include('oldcontrib.media.document.urls')),
    (r"^media/images/", include('oldcontrib.media.image.urls')),
    (r"^media/video/", include('oldcontrib.media.video.urls')),
)
