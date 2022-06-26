from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter # [14]
from rest_framework.urlpatterns import format_suffix_patterns # [14]

from . import views

app_name = 'movies'
urlpatterns = format_suffix_patterns([
    path("movie/", views.MovieViewSet.as_view({'get': 'list'})), # http://127.0.0.1:8001/api/v1/movie/
    path("movie/<int:pk>/", views.MovieViewSet.as_view({'get': 'retrieve'})), # http://127.0.0.1:8001/api/v1/movie/1
    path("review/", views.ReviewCreateViewSet.as_view({'post': 'create'})), # http://127.0.0.1:8001/api/v1/review/
    path("rating/", views.AddStarRatingViewSet.as_view({'post': 'create'})), # http://127.0.0.1:8001/api/v1/rating/ {"star":3, "movie": 1}
    # path("actors/", views.ActorsListView.as_view()), # http://127.0.0.1:8001/api/v1/actors/
    # path("actors/<int:pk>", views.ActorsDetailView.as_view()), # http://127.0.0.1:8001/api/v1/actors/1
    path("actor/", views.ActorsViewSet.as_view({'get': 'list'})), # [14] http://127.0.0.1:8001/api/v1/actor/
    path("actor/<int:pk>", views.ActorsViewSet.as_view({'get': 'retrieve'})), # [14] http://127.0.0.1:8001/api/v1/actor/1
])