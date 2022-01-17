
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
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


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/login.html/')
    else:
        form = UploadFileForm()
    return render(request, 'signuppro.html', {'form': form})


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
