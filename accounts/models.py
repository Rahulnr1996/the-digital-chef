from django.db import models

# Create your models here.
class registers(models.Model):
    firstname=models.CharField(max_length=250)
    lastname=models.CharField(max_length=250)
    username=models.CharField(max_length=300, unique=True)
    mail=models.EmailField()
    password1=models.CharField(max_length=300)
    password2=models.CharField(max_length=300)

