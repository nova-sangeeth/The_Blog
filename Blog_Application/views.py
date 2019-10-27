from django.shortcuts import render

from .models import posts


def Post_lists(request):
    # this is a database query set to show the data from the database.
    all_posts = posts.objects.all()
    context = {
        'all_posts': all_posts
    }
    return render(request, "posts_list.html", context)
