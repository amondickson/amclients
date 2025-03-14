from django.db import models
from django.contrib.auth.models import User
import datetime

class Record(models.Model):
    creation_date = models.DateTimeField(default=datetime.datetime.now)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=80)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    province = models.CharField(max_length=80)
    country = models.CharField(max_length=80)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    

    def __str__(self):
        return self.first_name + " " + self.last_name
