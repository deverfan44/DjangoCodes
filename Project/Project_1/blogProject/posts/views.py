from django.shortcuts import render, redirect
from .forms import PostFrom
from posts.models import Post

# Create your views here.
def add_post(request):
    if request.method == 'POST':
        new_post = PostFrom(request.POST)
        if new_post.is_valid():
            new_post.save(commit=True)
        return redirect('home')
    else:
        new_post = PostFrom()
    return render(request, 'posts/posts.html', {'form':new_post})

def edit_post(request, id):
    post = Post.objects.get(pk=id)
    edit_post = PostFrom(instance=post)
    if request.method == 'POST':
        edit_post = PostFrom(request.POST, instance=post)
        if edit_post.is_valid():
            edit_post.save(commit=True)
        return redirect('home')
    
    return render(request, 'posts/posts.html', {'form':edit_post})


def delete_post(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('home')
