from django.db import models
from django import forms

# Create your models here.
class keyboard(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='static/img/')

class drum(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='static/img/')

class guitar(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='static/img/')

class violin(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='static/img/')

class orders(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    item = models.CharField(max_length=50)
    id = models.IntegerField(primary_key=True)

class feedback(models.Model):
    name = models.CharField(max_length=50)
    feedback = models.CharField(max_length=300)
    rating = models.IntegerField()