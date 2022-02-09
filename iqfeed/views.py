
from .forms import PostModelForm
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from inquireme_2.models import Post


# def edit_post(request, pk=None):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostModelForm(request.POST,
#                              instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('edit_post')
#     else:
#         form = PostModelForm(instance=post)

#     return render(request,
#                   'edit_post.html',
#                   {
#                       'form': form,
#                       'post': post
#                   })


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
