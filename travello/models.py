from django.db import models

# Create your models here.
class Destination(models.Model):
  
  name = models.CharField(max_length = 100)
  img  = models.ImageField(upload_to = 'pics')
  desc = models.TextField()
  country = models.CharField(max_length = 100)
  price  = models.IntegerField()

class Place(models.Model):
  country = models.CharField(max_length = 100)
  img = models.ImageField(upload_to= 'pics')
  count = models.IntegerField()