from django.db import models

# Create your models here.

class user(models.Model):
    name=models.TextField()
    phone=models.TextField()
    email=models.TextField()
    password=models.TextField()
