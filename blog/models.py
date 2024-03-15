import datetime
from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=30, default="Anonymous")
    pub_date = models.DateTimeField("date published")

    def recent_pub(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def index_fpd(self):
        return self.pub_date.strftime('%d/%m/%Y')
    def post_fpd(self):
        return self.pub_date.strftime('')

    rating    = models.IntegerField(default=0)
    faves     = models.IntegerField(default=0)
    comments  = models.IntegerField(default=0)

    slug = models.SlugField(unique=True, max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=30)
    content = models.TextField(max_length=500)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.content
