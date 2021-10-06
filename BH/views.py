from django.http import response
from django.shortcuts import render

# Create your views here.
def home(response):
    return render(response, "website/home.html", {})

def wie_zijn_wij(response):
    return render(response, "website/wie.html", {})