from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse
from contact_us.form import ContactForm
from contact_us.models import Contact

# Create your views here.
class ContactView(TemplateView):
    template_name = "contact_us/contact-us.html"

class ContactCreate(CreateView):
    model = Contact
    template_name = 'contact_us/contact-us.html'
    form_class = ContactForm
    #def get_success_url(self):
        #return reverse('index')

