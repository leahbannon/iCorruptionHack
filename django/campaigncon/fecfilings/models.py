from django.db import models

class File(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField('date published')
    fecDate = models.DateTimeField('date published')

class Contribution(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField('date published')
    fecDate = models.DateTimeField('date published')
