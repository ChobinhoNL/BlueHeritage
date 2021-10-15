from django.shortcuts import render
from .models import Post
from .models import Kat

# Create your views here.
def home(response):
    return render(response, "website/home.html", {})

def wie_zijn_wij(response):
    return render(response, "website/wie.html", {})

def kittens(request):
    posts = Post.objects.all()
    return render(request, "website/kittens.html", {'posts': posts})

def post_detail(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except: 
        post=""
        print("No post found.")
    return render(request, "website/post_detail.html", {'post': post})

def verkoopvoorwaarden(response):
    return render(response, "website/verkoopvoorwaarden.html", {})

def onze_katten(request):
    katten = Kat.objects.all()
    return render(request, "website/onze_katten.html", {'katten': katten})