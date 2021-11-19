from django.db import models
from django.utils.text import slugify

from base.models import CommondBase
from tinymce.models import HTMLField

from tag.models import Tag

class Artikel(CommondBase):
    slug = models.SlugField(unique=True, max_length=60, editable=False, blank=True)
    title = models.CharField(max_length=60)
    content = HTMLField(max_length=5000)
    cover_image_url = models.URLField(max_length=250, blank=True)
    cover_intro = HTMLField(max_length=1000)
    tags = models.ManyToManyField(Tag)
    publish = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.slug is None or self.slug == '':
            self.slug = slugify(self.title)

        super(Artikel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title