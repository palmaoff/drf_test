# Django Rest Framework api
Simple api dev
# Installation
Firstly setup and activate virtual environment (example for Windows)
```
py -m venv env
.\env\Scripts\activate
```
Install Packages
```
pip install -r requirements.txt
```
Migrate database
```
cd backend
py manage.py makemigrations api
py manage.py migrate
Create superuser
```
py manage.py createsuperuser
```
```
Run dev server
```
py manage.py runserver
```
