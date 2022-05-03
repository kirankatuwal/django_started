import email
from django.db import models

# Create your models here.
class Contact(models.Model):
    username = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    address = models.CharField(max_length=122)
    city = models.CharField(max_length=122)
    state = models.CharField(max_length=122)
    zip = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()

