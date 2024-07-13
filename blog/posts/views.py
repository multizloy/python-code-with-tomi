from django.shortcuts import render
from .models import Post

# Create your views here.


def index(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "posts/index.html", context)


def post(request, pk):
    posts = Post.objects.get(id=pk)
    context = {"posts": posts}
    return render(request, "posts/posts.html", context)
