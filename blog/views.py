from django.shortcuts import render, get_object_or_404, redirect
from . models import Post
from . forms import PostForm
from django.utils import timezone

def post_list(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'blog/post_list.html', context)


def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post.id)
    else:
        form = PostForm()
    context = {'form':form}
    return render(request, 'blog/post_edit.html', context)


def post_edit(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post.id)
    else:
        form = PostForm(instance=post)
    context = {'form': form}
    return render(request, 'blog/post_edit.html', context)