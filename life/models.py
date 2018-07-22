from django.db import models

class Group(models.Model):
  established = models.DateTimeField(auto_now_add=True)
  name = models.CharField(max_length=50)
  
class Item(models.Model):
  name = models.CharField(max_length=50)
  date = models.DateTimeField(auto_now_add=True)
  description = models.CharField(max_length=200)

class User(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=10)