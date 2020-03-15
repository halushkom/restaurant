from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from account.models import Profile
from datetime import *
#from apiclient.discovery import build
#from google_auth_oauthlib.flow import InstalledAppFlow

class Order(models.Model):
    Name = models.CharField(max_length=50, null=True)
    PhoneNumber = models.CharField(max_length=13)
    Choice = models.CharField(max_length=10)
    Date = models.DateField(null=True)
    Time = models.TimeField(null=True, max_length=10)
    Mail = models.EmailField(max_length=100, null=True)
    def __str__(self):
        return self.Name
        #return self.Second_Name
