from django.db import models
from datetime import datetime

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    mobile = models.CharField(max_length=122)
    password = models.CharField(max_length=122)
    repassword = models.CharField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.name
