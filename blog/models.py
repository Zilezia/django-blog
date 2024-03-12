import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=30)
    pub_date = models.DateTimeField("date published")

    def recent_pub(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    faves = models.IntegerField(default=0)

    slug = models.SlugField(unique=True, max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    comment = models.CharField(max_length=400)
    com_likes = models.IntegerField(default=0)
    com_dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.comment
