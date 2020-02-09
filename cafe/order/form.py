from django import forms
from order.models import Order

class OrderForm(forms.ModelForm):
    Name = forms.CharField(required = True, help_text = "Введіть своє ім'я")
    Second_Name = forms.CharField(required = True, help_text = "Введіть своє Прізвище")
    PhoneNumber = forms.CharField(required = True, help_text = "Введіть номер мобільного")
    Description = forms.CharField(required = True, widget = forms.Textarea)
    Data_Time = forms.DateTimeField()
    class Meta:
        model = Order
        fields = ('Name', 'Second_Name', 'PhoneNumber', 'Description')
        labels = {
            'Name': "Ім'я",
            'SecondName': 'Прізвище',
            'PhoneNumber': 'Номер мобільного',
            'Description': 'Повідомлення',
        }