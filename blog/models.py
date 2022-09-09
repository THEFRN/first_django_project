from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    STATUS_CHOICES = (
        ('pub', 'Published'),
        ('drf', 'Draft'),
    )
    text = models.TextField()
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES)
    date_time_created = models.DateTimeField(auto_now_add=True)
    date_time_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
