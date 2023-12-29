import uuid

from django.conf import settings
from django.db import models
from django.utils.functional import cached_property

from coreapp.base import BaseModel
from utility import constants
from .utils import slug_utils


class GlobalSettings(BaseModel):
    site_name = models.CharField(max_length=100)
    website_url = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='website/', default='website/default.png')
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    short_desc = models.TextField(max_length=500)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    youtube = models.CharField(max_length=100, null=True, blank=True)

    @cached_property
    def get_logo_url(self):
        return f"{settings.MEDIA_HOST}{self.logo.url}"

    def __str__(self):
        return self.site_name


class Page(BaseModel):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    slug = models.CharField(max_length=100, unique=True, db_index=True, editable=False)
    thumbnail = models.ImageField(upload_to='page/', default='page/default.png')
    video_url = models.CharField(max_length=100, null=True, blank=True)
    page_type = models.IntegerField(choices=constants.PageType.choices)
    is_active = models.BooleanField(default=0)

    def __str__(self):
        return self.title

    @cached_property
    def get_thumbnail_url(self):
        return f"{settings.MEDIA_HOST}{self.thumbnail.url}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slug_utils.generate_unique_slug(self.title, self)
        super(Page, self).save(**kwargs)