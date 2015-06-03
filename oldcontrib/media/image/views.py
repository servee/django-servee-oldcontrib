from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.decorators import login_required

from oldcontrib.media.image.forms import ImageUpload

@csrf_exempt
def upload_image(request):
    """
    This view accepts 5 values (gallery, position, app_label, model, and pk) which are POSTed.
    Checks the values and adds the item at the specified position.
    """
    ret = {}
    ret['error'] = []

    img = ImageUpload(request.POST, request.FILES)
    if img.is_valid():
        image = img.save()
        ret['item'] = render_to_string('panels/add_image.html',dict(image=image))
    else:
        ret['error'].append('Not a valid form')
        ret['error'].append(img.errors)

    # return result
    resp = simplejson.dumps(ret)
    return HttpResponse(resp, mimetype='application/json')

@login_required
def recent_photos(request):
    images = [
        {"thumb": obj.image.url, "image": obj.image.url}
        for obj in Image.objects.all().order_by("-uploaded")[:20]
    ]
    return HttpResponse(json.dumps(images), mimetype="application/json")
