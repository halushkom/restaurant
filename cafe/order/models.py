from django.db import models

class Order(models.Model):
    Name = models.CharField(max_length=50, null=True)
    PhoneNumber = models.CharField(max_length=13)
    Choice = models.CharField(max_length=10)
    Date = models.DateField(null=True)
    Time = models.TimeField(null=True, max_length=10)
    Mail = models.EmailField(max_length=100, null=True)
    def __str__(self):
        return self.Name
