from django.shortcuts import render

from .models import Post


def Post_lists(request):
    # this is a database query set to show the data from the database.
    all_posts = Post.objects.all()
    context = {
        'all_posts': all_posts
    }
    return render(request, "posts_list.html", context)
