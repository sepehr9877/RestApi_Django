from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class AccountUser(models.Model):
    useraccount=models.ForeignKey(User,models.CASCADE)
    image=models.ImageField(null=True,blank=True,upload_to='User')
    country=models.CharField(null=True,blank=True,max_length=50)
    phone=models.CharField(null=True,blank=True,max_length=50)
    def __str__(self):
        return self.useraccount.username
