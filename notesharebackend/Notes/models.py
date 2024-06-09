from django.db import models
from User.models import User


class File(models.Model):
    filename = models.CharField(max_length=255)
    content = models.BinaryField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    user = models.CharField(max_length=255)
    #subject = models.CharField(max_length=255)