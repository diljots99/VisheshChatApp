from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


# Create your models here.

class contact(models.Model):
    firstname=models.CharField(max_length=122)
    lastname=models.CharField(max_length=122)
    subject=models.TextField()
    date=models.DateField()

class signupmodel(models.Model):
    first_name=models.CharField(max_length=122)
    last_name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    password=models.CharField(max_length=122)
    confirm_password=models.CharField(max_length=122)
    

