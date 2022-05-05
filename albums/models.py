from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    # image = models.FilePathField(path="/img")
    created_at = models.DateTimeField(auto_now_add=True)
    