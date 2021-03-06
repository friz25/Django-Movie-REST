# 1) Создание Django REST framework проэкта
создадим venv
зайдём в виртуальное окружение `python -m venv venv`

с терминала (venv/Scripts/activate):
```
pip install django
pip install pillow
pip install djangorestframework
pip install psycopg2-binary
```
Установим PostgreSQL. Запустим. Создадим таблицу `movie`

## В `settings.py` добавим:
```python
INSTALLED_APPS = [
'rest_framework',
]
```
Заменяем DATABASES:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db.name',
        'USER': 'user_name',
        'PASSWORD': 'pass',
        'HOST': 'localhost',
        'PORT':  '5432',
     }
}
```
Создаём папку `media`
```
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

## В `urls.py` добавим:
```
    path('api-auth/', include('rest_framework.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
### добавляем админа `python manage.py createsuperuser`
## в терминале `python manage.py migrate` !!

Зайдём на `http://127.0.0.1:8000/api-auth/login/`
Зайдём на `http://127.0.0.1:8000/admin/`

# 2) Видеоинструкция по переносу неREST проэкта сюда
https://www.youtube.com/watch?v=1DIDlsvv8cg&list=PLF-NY6ldwAWqSxUpnTBObEP21cFQxNJ7C&index=3

## * как изменить порт по умолчанию с 8000 на 80001
открываем `C:\Django\dm_rest\venv\Lib\site-packages\django\core\management\commands`

файл `runserver.py` изменить 8000 на 80001

# 3) Сериализация
`serializers.py`
`views.py`
`movies/urls.py`
фильтр фильмов (по годам и жанрам):
`pip install django-filter`
авторизация (обычные токены и JWT):
`pip install djoser`
`pip install djangorestframework_simplejwt`
прописать в `settings` и `urls`
сделать миграции

далее postman
http://127.0.0.1:8001/auth/token/login/
# АвтоДокументирование API
pip install drf-yasg
прописать в `settings`
http://127.0.0.1:8001/swagger/

## Добавление cors
*cors это для безопасности AJAX запросов <br>
Данная библиотека нам позволит добавлять к ответам заголовки Cross-Origin Resource Sharing (CORS). Это позволяет запросы в браузере к вашему приложению Django из других источников.

    pip install django-cors-headers 
прописать в `settings` <br>
в INSTALLED_APPS <br>
`'corsheaders',` <br>
в MIDDLEWARE <br>
`'corsheaders.middleware.CorsMiddleware',` <br>
внизу settings добавим настройку <br>
```python
CORS_ORIGIN_WHITELIST = [
    "http://localhost:8080",
    "http://127.0.0.1:8001",
]
```