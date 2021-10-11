from django.http import response
from django.shortcuts import render

# Create your views here.
def home(response):
    return render(response, "website/home.html", {})

def wie_zijn_wij(response):
    return render(response, "website/wie.html", {})

def kittens(response):
    return render(response, "website/kittens.html", {})

def verkoopvoorwaarden(response):
    return render(response, "website/verkoopvoorwaarden.html", {})
