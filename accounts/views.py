from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from inquire_me.forms import PostForm
from .forms import SignUpForm, SignUpProForm, LogInForm
from accounts.models import User
from inquire_me.models import Post
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)


def log_in(request):
    error = False
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                error = True
    else:
        form = LogInForm()

    return render(request, 'registration/login.html', {'form': form, 'error': error})


def logout_view(request):
    logout(request)
    return redirect('login')


def All_posts(request):
    return render(request, "feed.html")


# Create your views here.
User = get_user_model()


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def signuppro(request):
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


def LoginProView(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            user = User.objects.get(email=email)
            if user.password == form.cleaned_data['password']:
                login(request, user)
        return redirect('home')
    else:
        form = LogInForm()
        return render(request, 'registration/loginpro.html', {form: form})


def PostView(request):

    if request.method == 'POST':
        form = PostForm(request.POST, User)
        if form.is_valid():
            # Create post with form data
            newPost = Post()
            newPost.title = form.cleaned_data['title']
            newPost.body = form.cleaned_data['body']
            newPost.created_at = form.cleaned_data['created_at']
            newPost.categories = form.cleaned_data['categories']
            newPost.username = request.user
        # Save newPost
            newPost2 = newPost
            newPost2.save()
        # Redirect to index
        return redirect('feed')

    else:
        form = PostForm()
        return render(request, 'create_post.html', {'form': form})


class BlogPostDetailView(DetailView):
    model = Post
    template_name = 'feed.html'


class HomePageView(TemplateView):
    template_name = 'base.html'


class IQroomView(TemplateView):
    template_name = 'iqroom.html'


class SearchView(TemplateView):
    template_name = 'search.html'


# class IqNewView(CreateView):
#     model = Post
#     template_name = "create_post.html"
#     fields = ["title", "body", "picture"]


# class IqUpdateView(UpdateView):
#     model = Post
#     template_name = "edit_post.html"
#     fields = ["title", "body", "picture"]

#     def test_func(self):
#         obj = self.get_object()
#         return obj.username == self.request.user


# class IqDeleteView(DeleteView):
#     model = Post
#     template_name = "delete_post.html"
#     fields = ["title", "body", "picture"]

#     def test_func(self):
#         obj = self.get_object()
#         return obj.username == self.request.user


def All_posts(request):
    post_list = Post.objects.all()
    context = {
        'post_list': post_list,

    }
    return render(request, 'feed.html', context)


# def Color(request):
#     if request.method == "POST":
#         # Get Form Data
#         form = ColorForm(request.POST)
#         if form.is_valid():
#             # Create new user with form data
#             newColor = Color()
#             newColor.color = form.cleaned_data['color']
#             newColor.save()

#         # Redirect to index
#         return redirect('iqroom')
#     else:
#         form = ColorForm()
#         return render(request, 'iqroom.html', {'form': form})


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('feed', args=[str(pk)]))
