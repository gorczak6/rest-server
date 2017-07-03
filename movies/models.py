from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=128)


class Movie(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    director = models.ForeignKey(Person)
    actors = models.ManyToManyField(Person, through='MoviePerson', related_name='Actors')
    year = models.IntegerField()


class MoviePerson(models.Model):
    role = models.CharField(max_length=128)
    person = models.ForeignKey(Person)
    movie = models.ForeignKey(Movie)
