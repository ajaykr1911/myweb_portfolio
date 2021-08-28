from django.db import models
from datetime import datetime


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    desc = models.CharField(max_length=1000000)
    date = models.DateField()

    def __str__(self):
        return self.name

