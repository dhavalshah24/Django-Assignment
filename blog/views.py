from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post

# Create your views here.

def home(request) :

    posts = Post.objects.all()
    posts_paginator = Paginator(posts, 3)
    page_number = request.GET.get("page")
    page = posts_paginator.get_page(page_number)

    context = {
        "count" : posts_paginator.count,
        "page" : page
    }

    return render(request, "index.html", context)


def post_single(request, post) :

    post = get_object_or_404(Post, slug = post)
    return render(request, "single.html", {"post" : post})

def blogger(request) :

    all_posts = Post.objects.all().distinct()
    return render(request, "bloggers.html", {"posts" : all_posts})

def get_author_posts(request, id):

    author_posts = Post.objects.filter(author_id = id)
    return render(request, "author.html", {'posts':author_posts})