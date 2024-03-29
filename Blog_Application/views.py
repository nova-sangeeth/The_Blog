from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostModelForm
from .models import Post, Author


def Post_lists(request):
    # this is a database query set to show the data from the database.
    all_posts = Post.objects.all()
    context = {
        'all_posts': all_posts
    }
    return render(request, "posts_list.html", context)


def post_detail(request, slug):
    unique_post = get_object_or_404(Post, slug=slug)
    context = {
        'post': unique_post
    }
    return render(request, "posts_details.html", context)


def post_create(request):
    author, created = Author.objects.get_or_create(user=request.user,
                                                   email=request.user.email,
                                                   cellphone_num=12341234
                                                   )
    form = PostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.author = author
        form.save()
        return redirect('/posts_lists.html/')
    context = {
        'form': form
    }
    return render(request, "posts_create.html", context)


def post_update(request, slug):
  #  unique_post = get_object_or_404(Post, slug=slug)
    unique_post = Post, slug=slug
    form = PostModelForm(request.POST or None,
                         request.FILES or None,
                         instance=unique_post)
    if form.is_valid():
        form.save()
        return redirect('/posts_lists.html/')
    context = {
        'form': form
    }
    return render(request,"posts")

def post_delete(request,slug):
    unique_post = get_object_or_404(Post, slug=slug)
    unique_post.delete()
    return redirect('/posts_lists.html/')
