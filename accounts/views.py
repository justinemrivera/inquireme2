from django.shortcuts import redirect, render
from inquire_me.forms import PostForm
from .forms import SignUpForm, SignUpProForm, LoginForm
from django.contrib.auth import authenticate, login, logout, get_user_model
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
        return render(request, 'registration/signup.html', {'form': form})


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
        return render(request, 'registration/signuppro.html', {'form': form})


def LoginView(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password')
            User = authenticate(request, username=username, password=password)
            if User is not None:
                login(request, User)
                return redirect('iqfeed')
    else:
        form = LoginForm
    return render(request, 'registration/login.html', {'form': form})


# error when i hit submit on login.html
# ValueError at /login/
# The view accounts.views.LoginView didn't return an HttpResponse object. It returned None instead.


class HomePageView(TemplateView):
    template_name = 'base.html'


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
        print(form)
        if form.is_valid():
            # Create new user with form data
            newPost = Post()
            newPost.title = form.cleaned_data['title']
            newPost.body = form.cleaned_data['body']
            newPost.created_at = form.cleaned_data['created_at']
            newPost.User = form.cleaned_data['username']
            # newPost.picture = form.cleaned_data['picture']

        # Save new user
            newPost2 = newPost
            newPost2.save()

        # Redirect to index
        return redirect('iqfeed')
    else:
        form = PostForm()
        return render(request, 'create_post.html', {'form': form})


def All_posts(request):
    post_list = Post.objects.all()
    context = {
        'post_list': post_list
    }
    return render(request, 'feed.html', context)
