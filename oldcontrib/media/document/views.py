from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt

from oldcontrib.media.document.forms import DocumentUpload


@csrf_exempt
def upload_document(request):
    """
    This view accepts 5 values (gallery, position, app_label, model, and pk) which are POSTed.
    Checks the values and adds the item at the specified position.
    """
    ret = {}
    ret['error'] = []
    
    doc = DocumentUpload(request.POST, request.FILES)
    if doc.is_valid():
        document = doc.save()
        ret['item'] = render_to_string('panels/add_document.html',dict(document=document))
    else:
        ret['error'].append('Not a valid form')
        ret['error'].append(doc.errors)
    
    # return result
    resp = simplejson.dumps(ret)
    return HttpResponse(resp, mimetype='application/json')