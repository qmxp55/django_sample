# django_sample

## pyenv
Check python versions `pyenv versions` then choose one to create new environment and activate:

```bash
pyenv virtualenv 3.8.13 django_sample
pyenv activate django_sample 
```
> Note if `base` still there allong with `django_sample`, use `conda deactivate`.

## Steps

1. Create Project `django-admin startproject <projectname>`
2. Create App `python manage.py startapp <appname>`
3. Edit settings to add new apps
4. Create views 
5. Map urls

6. Create tables in models
7. `python manage.py migrate`
8. `python manage.py makemigrations my_app_1`
9. `python manage.py migrate`

10. import tables at `my_app_1/admin.py`
11. Create superuser with: `python manage.py createsuperuser `

## Django setup

Start project and run server
```
django-admin startproject carrentals
python manage.py runserver
```

## Create Apps

Create apps with

```
python manage.py startapp <appname>
```
inside the new app created we need to create the file `urls.py` and then, link it to main app urls file at `carrentals/urls.py`
