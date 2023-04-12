from django.db import models


# Create your models here.
class Computer(models.Model):
    mac_address = models.CharField(max_length=17)
    name = models.CharField(max_length=100)
