# TODO List for Implementing Book CRUD APIs in Django REST Framework

- [x] Edit myapp/models.py to add the Book model with fields: title (CharField), author (CharField), year_of_publish (IntegerField)
- [x] Create myapp/serializers.py with BookSerializer using ModelSerializer
- [x] Edit myapp/views.py to add BookViewSet using ModelViewSet for CRUD operations
- [x] Create myapp/urls.py to set up the router for BookViewSet
- [x] Edit myproject/urls.py to include myapp.urls
- [x] Run `python manage.py makemigrations` and `python manage.py migrate` to apply model changes

# New Task: Provide Dockerfile and docker-compose.yml for Docker deployment

- [x] Create Dockerfile for the Django app
- [x] Create docker-compose.yml for deployment
- [x] Update settings.py for PostgreSQL database
- [x] Update requirements.txt with psycopg2-binary
