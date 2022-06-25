from django.contrib import admin
from django.urls import path

from . import views

app_name = 'movies'
urlpatterns = [
    path("movie/", views.MovieListView.as_view()), # http://127.0.0.1:8001/api/v1/movie/
    path("movie/<int:pk>/", views.MovieDetailView.as_view()), # http://127.0.0.1:8001/api/v1/movie/1
    path("review/", views.ReviewCreateView.as_view()), # http://127.0.0.1:8001/api/v1/review/

]