from django.contrib import admin
from .models import Offspring, Post, Kat

# Register your models here.
admin.site.register(Post)
admin.site.register(Kat)
admin.site.register(Offspring)