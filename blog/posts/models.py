from django.db import models
from django.contrib.auth.models import User
# Create your models here.

import os
from django.utils.deconstruct import deconstructible

@deconstructible
class PathAndRename:
    def __init__(self, path):
        self.path = path

    def __call__(self, instance, filename):
        return os.path.join(self.path, filename)  # Zwraca oryginalną nazwę pliku

upload_to = PathAndRename('photos/')


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='photos/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    contents = models.TextField()
    
    def __str__(self):
        return f"comment by {self.author} on {self.post}"