from django import forms
from oldcontrib.media.video.models import Video

class VideoUpload(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('video',)