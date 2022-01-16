from django.shortcuts import render, redirect

from inquire_me.settings import LOGIN_REDIRECT_URL
from .models import Post
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)


class IqUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    login_url = '/login/'
    redirect_field_name = 'edit'
    template_name = "edit_post.html"
    fields = ["title", "body", "picture"]


class IqDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    login_url = '/login/'
    redirect_field_name = 'delete'
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")
