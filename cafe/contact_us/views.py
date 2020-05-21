from django.shortcuts import redirect
from django.views.generic import CreateView
from django.http import request
from contact_us.form import ContactForm
from contact_us.models import Contact
from django.contrib import messages
from cafe import settings

class contactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact_us/contact-us.html'

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, settings.MY_INFO, 'Дякуємо за Ваше звернення!')
        else:
            messages.add_message(request, settings.MY_INFO, "Заповніть обов'язові поля")
        return redirect("/")
