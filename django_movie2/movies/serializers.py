"""
СЕРИАЛИЗАТОРЫ - нужны чтоб приобразовывать типы данных python > в json (и наоборот)
"""
from rest_framework import serializers

from .models import Movie, Review

class MovieListSerializer(serializers.ModelSerializer):
    """ Список фильмов """

    class Meta:
        model = Movie
        fields = ("title", "tagline", "category")

class ReviewCreateSerializer(serializers.ModelSerializer):
    """[POST] Добавление комментария (к фильму) """

    class Meta:
        model = Review
        fields = "__all__"
class ReviewSerializer(serializers.ModelSerializer):
    """[GET] Вывод комментария (к фильму) """

    class Meta:
        model = Review
        fields = ("name", "text", "parent")

class MovieDetailSerializer(serializers.ModelSerializer):
    """ Полный фильмов """
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    directors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    actors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    genres = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        exclude = ("draft", )
