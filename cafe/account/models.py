from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length = 100, null = True, blank = True)
    street = models.CharField(max_length = 100, null = True, blank = True)
    home = models.CharField(max_length = 7, null = True, blank = False)
    post_code = models.CharField(max_length = 15, null = True, blank = False)


    def __str__(self):
        return self.user.username
        return self.user.location
        return self.user.first_name
        return self.user.last_name
        return self.user.email
        return self.user.street
        return self.user.home
        return self.user.post_code

