from django.db import models
from markup_mixin.models import MarkupMixin

class Chunk(MarkupMixin):
    """
    A Chunk is a piece of content associated
    with a unique key that can be inserted into
    any template with the use of a special template
    tag
    """
    key = models.CharField(help_text="A unique name for this chunk of content", blank=False, max_length=255, unique=True)
    content = models.TextField(blank=True)
    rendered_content = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u"%s" % (self.key,)

    class MarkupOptions:
        source_field = 'content'
        rendered_field = 'rendered_content'
