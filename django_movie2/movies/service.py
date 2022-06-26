from django_filters import rest_framework as filters # дописали [10]
from .models import Movie # дописали [10]

def get_client_ip(request):
    """ Получение IP пользователя """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    """ [10] """
    pass

class MovieFilter(filters.FilterSet):
    """ [10] """
    genres = CharFilterInFilter(field_name='genres__name', lookup_expr='in')
    year = filters.RangeFilter()

    class Meta:
        model = Movie
        fields = ['genres', 'year']
