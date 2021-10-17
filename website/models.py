from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title

class Kat(models.Model):
    naam = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to="katten/")
    geboortedatum = models.CharField(max_length=10)
    vader = models.CharField(max_length=255)
    moeder = models.CharField(max_length=255)
    BSH = models.CharField(max_length=10)

    def __str__(self):
        return self.naam

class Offspring(models.Model):
    naam = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to="offspring/")
    
    def __str__(self):
        return self.naam