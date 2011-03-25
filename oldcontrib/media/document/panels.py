from django.conf import settings
from django.template.loader import render_to_string
from oldcontrib.media.document.forms import DocumentUpload
from oldcontrib.media.document.models import Document
from servee.wysiwyg.panels import InsertPanel

class DocumentPanel(InsertPanel):
    
    name = 'Document'
    has_content = True
    
    def nav_title(self):
        return 'Document'

    def title(self):
        return 'Document'
        
    def content(self):
        documents = Document.objects.all()
        form = DocumentUpload()
        
        context = self.context.copy()
        context.update(dict(documents=documents, form=form, STATIC_URL=settings.STATIC_URL))
        return render_to_string('panels/document.html', context)

    def url(self):
        return '#insert_document'