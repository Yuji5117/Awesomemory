from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SignupForm, ProfileForm, UserUpdateForm, ProfileUpdateForm
from .models import UserProfile


class SignupView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('post:post')
    template_name = 'registration/signup.html'

class UserProfileView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'registration/user_profile.html'

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = ProfileUpdateForm
    template_name = 'registration/user_profile_update.html'
    # success_url = reverse_lazy('accounts:profile')

    def get_success_url(self):
        return resolve_url('accounts:profile', pk=self.kwargs['pk'])





