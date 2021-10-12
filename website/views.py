from django.shortcuts import render
from .models import Post

# Create your views here.
def home(response):
    return render(response, "website/home.html", {})

def wie_zijn_wij(response):
    return render(response, "website/wie.html", {})

def kittens(request):
    posts = Post.objects.all()
    return render(request, "website/kittens.html", {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "website/post_detail.html", {'post': post})

def verkoopvoorwaarden(response):
    return render(response, "website/verkoopvoorwaarden.html", {})
