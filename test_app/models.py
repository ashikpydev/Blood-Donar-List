from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BloodDonar(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)   
    name = models.CharField(max_length=50, blank = True, null = True)
    image = models.ImageField(upload_to= 'profile_pics' ,blank = True, null = True)
    blood_group = models.CharField(max_length=50, blank = True, null = True)
    phone = models.CharField(max_length=50, blank = True, null = True)
    address = models.TextField(blank = True, null = True)
    profession = models.CharField(max_length=50, blank = True, null = True)
    email = models.EmailField(max_length=254, blank = True, null = True)
    facebook_link = models.CharField(max_length=50, blank = True, null = True)
    

    def __str__(self):
        return self.name


    
