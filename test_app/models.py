from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BloodDonar(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)   
    name = models.CharField(max_length=50, blank = True, null = True)
    blood_group = models.CharField(max_length=50, blank = True, null = True)
    phone = models.CharField(max_length=50, blank = True, null = True)


    def __str__(self):
        return self.name
    