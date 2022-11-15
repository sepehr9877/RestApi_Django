from django.db import models

# Create your models here.
class Products(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='Products',null=True,blank=True)

    def __str__(self):
        return self.title
