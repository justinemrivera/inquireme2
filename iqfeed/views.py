
from .forms import PostModelForm
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from inquireme_2.models import Post


# def create_post(request):
#     if request.method == 'POST':
#         form = PostModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('create_post')
#     else:
#         form = PostModelForm()
#     return render(request,
#                   'templates/create_post.html',
#                   {
#                       'form': form
#                   })


def showform(request):
    form = PostModelForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form': form}

    return render(request, 'templates/feed.html', context)


def edit_post(request, pk=None):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostModelForm(request.POST,
                             instance=post)
        if form.is_valid():
            form.save()
            return redirect('edit_post')
    else:
        form = PostModelForm(instance=post)

    return render(request,
                  'templates/edit_post.html',
                  {
                      'form': form,
                      'post': post
                  })


# def delete_post(request, pk=None):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostDeleteForm(request.POST,
#                               instance=post)
#         if form.is_valid():
#             post.delete()
#             return redirect('post_create')
#     else:
#         form = PostDeleteForm(instance=post)

#     return render(request, 'blog/post_delete.html',
#                   {
#                       'form': form,
#                       'post': post,
#                   })
