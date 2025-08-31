# Django REST Framework: School System API

This project is a simple RESTful API built using **Python** and **Django REST Framework (DRF)**, designed for a school system. It demonstrates how to create models, serializers, views, and viewsets, as well as integrate Django Admin and implement authentication and permissions.
===============================================

*Prerequisites* <br>
- Python 3.x <br>
- Django 4.2.11 <br>
- Django REST Framework <br>
- Markdown (for DRF browsable API support) <br>

## Features

- Create models and serializers
- Build API endpoints using Views or ViewSets
- When to use Views vs ViewSets
- Implement Routers for route handling
- Add authentication and permission classes
- Integrate Django Admin with your API
- Handle API root for better navigation

## Setup Instructions

```bash
# Create a Virtual Environment
python -m venv venv
```

```bash
# Activate the Virtual Environment
# Windows
vvenv\Scripts\activate.bat

# macOS/Linux
source venv/bin/activate
```

```bash
# Install Requirements
pip install django==4.2.11
pip install djangorestframework
pip install markdown
```

```bash
# Create Django Project
django-admin startproject setup .
```

```bash
# Create Django App
python manage.py startapp school
```

```bash
# Apply Migrations
python manage.py makemigrations
python manage.py migrate
```

```bash
# Create Superuser
python manage.py createsuperuser
```

```bash
# Test Django Shell
python manage.py shell
```

```bash
# Example imports
from school.models import Student
from school.serializers import StudentSerializer
```

```bash
# Create requirements.txt
pip freeze > requirements.txt
```

```bash
# Run server
python manage.py runserver
```

## Example API Requests
### List Students
```bash
curl -X GET http://127.0.0.1:8000/students/ -u username:password

curl -X POST http://127.0.0.1:8000/students/ \
-H "Content-Type: application/json" \
-d '{"name":"John Doe","email":"john@example.com"}' \
-u username:password
```

## Author
 | [<img src="https://avatars1.githubusercontent.com/u/46221221?s=460&u=0d161e390cdad66e925f3d52cece6c3e65a23eb2&v=4" width=115><br><sub>@jacksonn455</sub>](https://github.com/jacksonn455) |
  | :---: |
