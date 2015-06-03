import json

from django.http import HttpResponse
from django.template.loader import render_to_string

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from django.contrib.auth.decorators import login_required

from oldcontrib.media.image.forms import ImageUpload
from oldcontrib.media.image.models import Image

@csrf_exempt
@require_POST
@login_required
def upload_image(request):
    images = []
    for f in request.FILES.getlist("file"):
        obj = Image.objects.create(image=f)
        images.append({"filelink": obj.image.url})
    return HttpResponse(json.dumps(images), mimetype="application/json")

@login_required
def recent_photos(request):
    images = [
        {"thumb": obj.image.url, "image": obj.image.url}
        for obj in Image.objects.all().order_by("-uploaded")[:20]
    ]
    return HttpResponse(json.dumps(images), mimetype="application/json")
