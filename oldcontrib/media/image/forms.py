from django import forms
from oldcontrib.media.image.models import Image

class ImageUpload(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)