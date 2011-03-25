from django.contrib import admin
from oldcontrib.media.video.models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
admin.site.register(Video, VideoAdmin)
