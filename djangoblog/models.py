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