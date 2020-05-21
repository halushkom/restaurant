from django.db import models

class Contact(models.Model):
    Name = models.CharField(max_length=50, null = True)
    Mail = models.EmailField(max_length=100, null = True)
    Message = models.TextField(max_length = 500, null = True )
    def __str__(self):
        return self.Name
    class Meta():
        verbose_name_plural = "Форма зворотнього зв'язку"