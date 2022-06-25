"""
СЕРИАЛИЗАТОРЫ - нужны чтоб приобразовывать типы данных python > в json (и наоборот)
"""
from rest_framework import serializers

from .models import Movie

class MovieListSerializer(serializers.ModelSerializer):
    """ Список фильмов """

    class Meta:
        model = Movie
        fields = ("title", "tagline", "category")

class MovieDetailSerializer(serializers.ModelSerializer):
    """ Полный фильмов """

    class Meta:
        model = Movie
        fields = ("draft", )