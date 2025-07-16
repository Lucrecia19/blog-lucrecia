from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProfileForm
from django.views.generic import TemplateView 
from django.contrib.auth.mixins import LoginRequiredMixin 
from django import forms

from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileForm


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['user'] =self.request.user
        context['profile'] = self.request.user.profile
        return context

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['first_name', 'last_name', 'email']

@login_required
def profile_view(request):
     return render(request, 'accounts/profile.html')

@login_required
def edit_profile(request):
    user = request.user
    profile = user.profile
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/edit_profile.html', {'form': form})
    