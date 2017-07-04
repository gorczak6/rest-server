from rest_framework import serializers

from .models import Movie, Person, MoviePerson


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    director = PersonSerializer()
    actors = PersonSerializer()

    class Meta:
        model = Movie
        fields = '__all__'


class MoviePersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviePerson
        fields = '__all__'

