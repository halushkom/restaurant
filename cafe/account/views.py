from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from .models import Profile
from django.contrib.auth import login, authenticate


# Create your views here.
class ProfileDetailView(DetailView):
    template_name = 'account/profile.html'
    model = Profile
    context_object_name = 'profile'
    pk_url_kwarg = 'profile_id'

class SignUP(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        #create user
        created_user = form.save()
        # create profile
        profile = Profile.objects.create(user=created_user)
        # Authenticate user добуваємо логін і пароль з кешу
        autenticated_user = authenticate(
            username = form.cleaned_data.get('username'),
            password = form.cleaned_data.get('password1'),
        )
        login(self.request, autenticated_user)
        return redirect('profile', profile.id)