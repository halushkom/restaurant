from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from account.models import Profile
#from apiclient.discovery import build
#from google_auth_oauthlib.flow import InstalledAppFlow

class Order(models.Model):
    #scope = ['https://wwww.googleapis.com/auth/calendar']
    #flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', scope=scope)
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    Name = models.CharField(max_length=50, null=True)
    Second_Name = models.CharField(max_length=50,null=True)
    PhoneNumber = models.CharField(max_length=13)
    Description = RichTextUploadingField(max_length=150, null=True, blank=True)
    Data_Time = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.Name
        #return self.Second_Name
