from django.db import models

# Create your models here.

from django.db import models

class Movies(models.Model):
    movie_name=models.CharField(max_length=250)
    year=models.CharField(max_length=200)
    runtime=models.CharField(max_length=200)
    language=models.CharField(max_length=250)
    genres=models.CharField(max_length=200)
    poster_image=models.ImageField(upload_to="images",null=True,blank=True)
    description=models.CharField(max_length=250,null=True)

    def __str__(self):
        return self.movie_name