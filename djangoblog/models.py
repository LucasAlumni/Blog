from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateTimeField('date published')

    def __str__(self):
        return '%s' % self.title

    def was_published_recently(self):
        return self.posted >= timezone.now() - datetime.timedelta(days=1)


class Comment(models.Model):
    name = models.CharField(max_length=42)
    text = models.TextField()
    post = models.ForeignKey(Blog)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text