# Создание Django REST framework проэкта
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

## Видеоинструкция по переносу неREST проэкта сюда
https://www.youtube.com/watch?v=1DIDlsvv8cg&list=PLF-NY6ldwAWqSxUpnTBObEP21cFQxNJ7C&index=3
