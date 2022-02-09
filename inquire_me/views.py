

from accounts.models import CATEGORY_CHOICES
from inquire_me.models import Post
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .models import Post, Comment, Category
from .forms import NewCommentForm

from inquire_me.settings import LOGIN_REDIRECT_URL
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


class IqUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    redirect_field_name = 'feed'
    template_name = "edit_post.html"
    fields = ["title", "body", "picture"]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class IqDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    redirect_field_name = 'feed'
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/success/login.html/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'signuppro.html', {'form': form})


# def handle_uploaded_file(f):
#     with open('some/file/name.txt', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comments_connected = Comment.objects.filter(
            post_connected=self.get_object()).order_by('-date_posted')
        data['comments'] = comments_connected
        if self.request.user.is_authenticated:
            data['comment_form'] = NewCommentForm(instance=self.request.user)

        return data

    def post(self, request, *args, **kwargs):
        new_comment = Comment(content=request.POST.get('content'),
                              author=self.request.user,
                              post_connected=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)


def CategoryDetailView(request, cats):
    category_posts = Post.objects.filter(categories=cats)
    return render(request, 'category_detail.html', {'cats': cats.title(), 'category_posts': category_posts})


def cat(request):
    my_model = Category.objects.all()
    return render(request, 'base.html', {'my_model': my_model, 'cats': Category.CATEGORY_CHOICES})
