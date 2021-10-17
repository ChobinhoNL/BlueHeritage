"""BH URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from BH import views
from website import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("wie_zijn_wij/", views.wie_zijn_wij, name="wie_zijn_wij"),
    path("kittens/", views.kittens, name="kittens"),
    path("verkoopvoorwaarden/", views.verkoopvoorwaarden, name="verkoopvoorwaarden"),
    path("blog/<slug:slug>/", views.post_detail, name="post_detail"),
    path("onze_katten/", views.onze_katten, name="onze_katten"),
    path("onze_offspring/", views.onze_offspring, name="onze_offspring"),
]

