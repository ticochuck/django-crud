# Django Models

[Link to Latest PR](https://github.com/ticochuck/django_crud/pull/1)

## Description

Create a django project with and app and with full CRUD functionallity.


## Usage

- `poetry shell` to start your virtual environment
- `poetry install` to install dependencies
- create .env file with the following variables and save it into 'snacks_project' directory
    - SECRET_KEY=secret key for the app (typically 50-characters long string)
    - DEBUG=should be set to True in development
    - ALLOWED_HOSTS=localhost,127.0.0.1 (for testing)
- `python manage.py makemigrations` - to generate DB schema
- `python manage.py migrate` - to create DB schema
- `python manage.py createsuperuser` - to create user with admin access
- `python manage.py collectstatic` - to collect apps static files
- `python manage.py runserver` - to run server

## Tests
Use Django’s built in testing tools
- Test home page route 
- Test home page template

## Lab28 - Django CRUD

[Canvas Assignment](https://canvas.instructure.com/courses/2045906/assignments/15160046)

## Author

[Chuck Li Villalobos](https://github.com/ticochuck)


## References
[Generic Views](https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-editing/#django.views.generic.edit.UpdateView)