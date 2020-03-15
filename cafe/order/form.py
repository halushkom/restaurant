from django import forms
from order.models import Order
from datetime import *
class OrderForm(forms.ModelForm):
    choice = [
        ('1','1 персона'), ('2','2 персони'), ('3','3 персони'), ('4','4 персони'), ('5','5 персон'), ('6','6 персон')
    ]
    Name = forms.CharField(required = True )
    PhoneNumber = forms.CharField(required = True)
    Mail = forms.EmailField()
    Date = forms.DateField(widget=forms.SelectDateWidget)
    Time = forms.TimeInput(format='%H:%M')
    Choice = forms.ChoiceField(choices=choice)
    class Meta:
        model = Order
        fields = ('Name', 'PhoneNumber', 'Choice', 'Date', 'Time')
        labels = {
            'Name': "Ім'я",
            'PhoneNumber': 'Номер мобільного',
            'Choice': 'Вибір',
            'Time': 'Час'
        }