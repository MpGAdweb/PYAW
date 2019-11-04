from django.db import models
import datetime

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    slug = models.SlugField()
    client_url = models.CharField(max_length=200, null=True, blank=True)
    soluctions = models.TextField(max_length=400, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    project_date = models.DateField()
    cover1 = models.ImageField(upload_to='images/')
    cover2 = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.client
