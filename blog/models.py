from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField(default='')
    pub_date=models.DateTimeField(default=timezone.now)
    writer=models.TextField(default='')
    image=models.ImageField(upload_to='images/', blank=True)
    category=models.CharField(default='', max_length=255)