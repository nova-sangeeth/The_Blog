"""The_Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Blog_Application.views import Post_lists, post_detail, post_create, post_update, post_delete

# the views function is used from the views files.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', Post_lists),
    path('create/', post_create),
    path('post_update/<slug:slug>', post_update, name='post_update'),
    path('post_delete/<slug:slug>', post_delete, name='post_delete'),
    path('post_detail/<slug:slug>', post_detail, name='post_detail'),
]
