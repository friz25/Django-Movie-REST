from django.db import models # дописали [6]
from rest_framework import generics, permissions, viewsets # [14]
# from rest_framework.response import Response # удалили [9]
# from rest_framework.views import APIView # удалили [9]
from django_filters.rest_framework import DjangoFilterBackend

from .models import Movie, Actor
from .serializers import (
    MovieListSerializer,
    MovieDetailSerializer,
    ReviewCreateSerializer,
    CreateRatingSerializer,
    ActorListSelializer,
    ActorDetailSelializer
)
from .service import get_client_ip, MovieFilter
'''
class MovieListView(generics.ListAPIView):
    """ [GET] Вывод списка фильмов [11]"""
    serializer_class = MovieListSerializer
    filter_backends = (DjangoFilterBackend,) #подключили фильт django
    filterset_class = MovieFilter # http://127.0.0.1:8001/api/v1/movie/?year_min=1983&year_max=2022&genres=Боевик
    permission_classes = [permissions.IsAuthenticated] # [12]

    def get_queryset(self):
        movies = Movie.objects.filter(draft=False).annotate(
            rating_user=models.Count("ratings", filter=models.Q(ratings__ip=get_client_ip(self.request)))
        ).annotate(
            middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
        )
        return movies
'''

"""###########################################################################
*ReadOnlyModelViewSet - может выводить и список и одну запись
###########################################################################"""

class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    """ [GET] Вывод списка фильмов [14] \n
    * ReadOnlyModelViewSet - может выводить и список и одну запись """
    filter_backends = (DjangoFilterBackend,) #подключили фильт django
    filterset_class = MovieFilter # http://127.0.0.1:8001/api/v1/movie/?year_min=1983&year_max=2022&genres=Боевик

    def get_queryset(self):
        movies = Movie.objects.filter(draft=False).annotate(
            rating_user=models.Count("ratings", filter=models.Q(ratings__ip=get_client_ip(self.request)))
        ).annotate(
            middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
        )
        return movies

    def get_serializer_class(self):
        if self.action == 'list':
            return MovieListSerializer
        elif self.action == 'retrieve':
            return MovieDetailSerializer
'''[v1]
class MovieDetailView(APIView):
    """ [GET] Вывод фильма """
    def get(self, request, pk):
        movie = Movie.objects.get(id=pk, draft=False)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)
'''
'''[v2]
class MovieDetailView(generics.RetrieveAPIView):
    """ [GET] Вывод фильма [9]"""
    queryset = Movie.objects.filter(draft=False)
    serializer_class = MovieDetailSerializer
'''
'''[v1]
class ReviewCreateView(APIView):
    """ [POST] Добавление комментария (к фильму) """
    def post(self, request):
        review = ReviewCreateSerializer(data=request.data)
        if review.is_valid():
            review.save()
        return Response(status=201)
'''
'''[v2]
class ReviewCreateView(generics.CreateAPIView):
    """ [POST] Добавление комментария (к фильму) [9]"""
    serializer_class = ReviewCreateSerializer
'''

"""###########################################################################
*ModelViewSet - позволяет нам реализ-ть сразу добавление, вывод списка, одной записи, обновления, удаления записи 
###########################################################################"""

class ReviewCreateViewSet(viewsets.ModelViewSet):
    """ [POST] Добавление комментария (к фильму) [14]"""
    serializer_class = ReviewCreateSerializer
'''[v1]
class AddStarRatingView(APIView):
    """[POST] Добавление рейтинга фильму """

    def post(self, request):
        serializer = CreateRatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ip=get_client_ip(request))
            return Response(status=201)
        else:
            return Response(status=400)
'''
'''[v2]
class AddStarRatingView(generics.CreateAPIView):
    """[POST] Добавление рейтинга фильму """
    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        """ возвращает IP пользователя """
        serializer.save(ip=get_client_ip(self.request))
'''
class AddStarRatingViewSet(viewsets.ModelViewSet):
    """[POST] Добавление рейтинга фильму """
    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        """ возвращает IP пользователя """
        serializer.save(ip=get_client_ip(self.request))
'''[v1]
class ActorsListView(generics.ListAPIView):
    """ Вывод списка актёров [8] """
    queryset = Actor.objects.all()
    serializer_class = ActorListSelializer

class ActorsDetailView(generics.RetrieveAPIView):
    """ Вывод полного описания актёра / режжисёра [8] """
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSelializer
'''
class ActorsViewSet(viewsets.ReadOnlyModelViewSet):
    """" Вывод списка актёров [8] """
    queryset = Actor.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ActorListSelializer
        elif self.action == 'retrieve':
            return ActorDetailSelializer