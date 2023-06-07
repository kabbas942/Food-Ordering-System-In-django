from django.db import models
from baseFiles.models import BaseModel
from django.contrib.auth.models import User
# Create your models here.


class Profile(BaseModel):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="profile")
    is_email_verified = models.BooleanField(default=False)
    address =models.CharField(max_length=200,null=True,blank=True)
    zipCode=models.CharField(max_length=100,null=True,blank=True)
    mobileNumber=models.CharField(max_length=100,null=True,blank=True)
    