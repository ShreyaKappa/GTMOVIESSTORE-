from django.db import models
from movies.models import Movie

class Region(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


class MovieViewCount(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    purchases = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.movie.name} in {self.region.name}"
