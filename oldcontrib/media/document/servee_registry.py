from servee import frontendadmin
from servee.frontendadmin.insert import ModelInsert
from oldcontrib.media.document.models import Document

class DocumentInsert(ModelInsert):
    model = Document

frontendadmin.site.register_insert(DocumentInsert)