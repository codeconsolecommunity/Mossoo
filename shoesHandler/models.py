from django.db import models

# Create your models here.
class Shoes(models.Model):
    price = models.IntegerField()
    img = models.ImageField()
    model = models.TextField(null=False, blank=False)
    mark = models.CharField(max_length=100, null=False, blank=False)
    color = models.CharField(max_length=100, null=False, blank=False)
    sex = models.CharField(max_length=3, null=False, blank=False)
    numberOfItem = models.IntegerField()
    category= models.CharField(max_length=100, null=False, blank=False)
