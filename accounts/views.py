from django.shortcuts import redirect, render

from inquire_me.forms import PostForm
from .forms import SignUpForm, LoginForm, SignUpProForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, get_user_model
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from accounts.models import User
from inquire_me.models import Post
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)


# Create your views here.
User = get_user_model()


class HomePageView(TemplateView):
    template_name = "base.html"


# class SignUpView(generic.CreateView):
#     model = User
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registrations/signup.html'


def SignUpView(request):
    if request.method == "POST":
        # Get Form Data
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Create new user with form data
            newUser = User()
            newUser.name = form.cleaned_data['name']
            newUser.email = form.cleaned_data['email']
            newUser.password = form.cleaned_data['password']
            newUser.username = form.cleaned_data['username']
        # Save new user
            newUser.save()

        # Redirect to index
        return redirect('login')
    else:
        form = SignUpForm()
        return render(request, 'registrations/signup.html', {'form': form})


def SignUpProView(request):
    if request.method == "POST":
        # Get Form Data
        form = SignUpProForm(request.POST)
        if form.is_valid():
            # Create new user with form data
            newUser = User()
            newUser.first_name = form.cleaned_data['first_name']
            newUser.last_name = form.cleaned_data['last_name']
            newUser.email = form.cleaned_data['email']
            newUser.password = form.cleaned_data['password']
            newUser.username = form.cleaned_data['username']
            newUser.birth_date = form.cleaned_data['birth_date']
            newUser.CATEGORY_VERIFIED = form.cleaned_data['category_verified']

        # Save new user
            newUser.save()

        # Redirect to index
        return redirect('login')
    else:
        form = SignUpProForm()
        return render(request, 'registrations/signuppro.html', {'form': form})


def LoginView(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = User.objects.get(username=username)
            if user.password == form.cleaned_data['password']:
                login(request, user)
        return redirect('iqfeed')
    else:
        form = LoginForm()
        return render(request, 'registrations/login.html', {form: form})

# class LoginView(generic.CreateView):
#     form_class = UserCreationForm
#     template_name = 'registrations/login.html'


# class FeedView(TemplateView):
#   template_name = 'feed.html'


class IQroomView(TemplateView):
    template_name = 'iqroom.html'


class SearchView(TemplateView):
    template_name = 'search.html'


class IqNewView(CreateView):
    model = Post
    template_name = "create_post.html"
    fields = ["title", "body", "picture"]


class IqUpdateView(UpdateView):
    model = Post
    template_name = "edit_post.html"
    fields = ["title", "body", "picture"]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class IqDeleteView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    fields = ["title", "body", "picture"]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


def PostView(request):
    if request.method == "POST":
        # Get Form Data
        form = PostForm(request.POST)
        if form.is_valid():
            # Create new user with form data
            newPost = Post()
            newPost.title = form.cleaned_data['title']
            newPost.body = form.cleaned_data['body']
            newPost.created_at = form.cleaned_data['created_at']
            newPost.username = form.cleaned_data['username']
            newPost.CATEGORY_VERIFIED = form.cleaned_data['category_verified']
            newPost.picture = form.cleaned_data['picture']

        # Save new user
            newPost.save()

        # Redirect to index
        return redirect('iqfeed')
    else:
        form = PostForm()
        return render(request, 'create_post.html', {'form': form})


def All_posts(request):
    post_list = Post.objects.all()
    context = {
        'post_list': post_list,
    }
    return render(request, 'feed.html', context)


# class FeedView(ListView):
#     template_name = 'feed.html'

#     def get_queryset(self):
#         return Post.objects.all()
