from django.contrib.auth.models import User
from django.db import models

# Create your models here.
##you have to make related_name field
class Products(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='owner')
    highlited=models.TextField(null=True,blank=True)
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='Products',null=True,blank=True)

    def __str__(self):
        return self.title
