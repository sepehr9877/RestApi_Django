from django.db import models
from Account.models import AccountUser

class Content(models.Model):
    user_content=models.ForeignKey(AccountUser,on_delete=models.CASCADE,null=True,blank=True)
    content=models.CharField(max_length=300)
    created_date=models.DateTimeField(auto_created=True,auto_now_add=True)
    def __str__(self):
        return self.user_content.useraccount.username
# Create your models here.
