from django import forms
from contact_us.models import Contact

class ContactForm(forms.ModelForm):
    Name = forms.CharField(required = True)
    Mail = forms.EmailField()
    Message = forms.CharField(widget=forms.Textarea, required = True)
    class Meta:
        model = Contact
        fields = ('Name', 'Mail', 'Message')