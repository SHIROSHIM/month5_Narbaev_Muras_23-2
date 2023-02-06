from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=200)
    # Add other fields as needed

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=200)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    # Add other fields as needed

    def __str__(self):
        return self.name

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField(default=0)
    # Add other fields as needed

    def __str__(self):
        return f'{self.movie} ({self.stars})'
