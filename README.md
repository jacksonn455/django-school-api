# Django REST Framework: Building RESTful APIs

This project is a simple RESTful API built using **Python** and **Django REST Framework (DRF)**. It demonstrates how to create models, serializers, views, and viewsets, as well as integrate Django Admin and implement authentication and permissions.

---

## Features

- Create models and serializers
- Build API endpoints using ViewSets and Routers
- Integrate Django Admin with your API
- Add authentication and permission classes
- Handle API root for better navigation

---

## Requirements

- Python 3.x
- Django 4.2.11
- Django REST Framework
- Markdown (for DRF browsable API support)

---

## Setup Instructions

## 1. Create a Virtual Environment

python -m venv venv

## Activate the Virtual Environment
# Windows
venv\Scripts\activate.bat

# macOS/Linux
source venv/bin/activate

## Requirements

- pip install django==4.2.11
- pip install djangorestframework
- pip install markdown


## Create Django Project
- django-admin startproject setup .

## Create Django App
- python manage.py startapp school

## Apply Migrations
- python manage.py makemigrations
- python manage.py migrate

## Create Superuser
- python manage.py createsuperuser

## Test Django Shell
- python manage.py shell

# Example imports
- from school.models import Student
- from school.serializers import StudentSerializer

# Create requirements.txt
- pip freeze > requirements.txt
