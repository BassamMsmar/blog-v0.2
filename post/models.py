from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=200)


    def __str__(self):
        return str(self.title)