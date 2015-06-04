import json

from django.http import HttpResponse
from django.template.loader import render_to_string

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from django.contrib.auth.decorators import login_required

from oldcontrib.media.document.forms import DocumentUpload
from oldcontrib.media.document.models import Document

@csrf_exempt
@require_POST
@login_required
def upload_document(request):
    documents = []
    for f in request.FILES.getlist("file"):
        obj = Document.objects.create(document=f)
        documents.append({"filelink": obj.document.url})
    return HttpResponse(json.dumps(documents), mimetype="application/json")

@login_required
def recent_documents(request):
    documents = [
        {"thumb": obj.document.url, "document": obj.document.url, "title": obj.title, "name": obj.document.name, "link": obj.document.url, "size": obj.document.size}
        for obj in Document.objects.all().order_by("-uploaded")[:20]
    ]
    return HttpResponse(json.dumps(documents), mimetype="application/json")