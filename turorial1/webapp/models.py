from django.db import models

class Record(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    province = models.CharField(max_length=80)
    country = models.CharField(max_length=80)

    def __str__(self):
        return self.first_name + "   "+self.last_name
