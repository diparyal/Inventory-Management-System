from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser): 
   username = models.CharField(max_length = 50, blank = True, null = True, unique = True) 
   email = models.EmailField(max_length = 25, unique = True) 
   
   phone_no = models.CharField(max_length = 10) 
   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = ['username'] 

   # objects = UserManager()

   def __str__(self): 
       return "{}".format(self.email) 