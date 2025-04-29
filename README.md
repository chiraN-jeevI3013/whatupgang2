# Hi, welcome to WhatUpGang

## Initializing the project:

#### 1. Create project folder
```
mkdir whatupgang
cd whatupgang
```

#### 2. Create virtual environment
```
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Django
```
pip install django
```

#### 4. Start Django project
```
django-admin startproject config .
```

#### 5. Start 2 apps
```
python manage.py startapp users
python manage.py startapp teams
```

## Adding Git Ignore file
#### .gitignore
```
# Python/Django
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
*.sqlite3
*.log

# macOS
.DS_Store
```

## Applying Migrations
```
python manage.py makemigrations users teams
python manage.py migrate
```


## Running the server
```
python manage.py runserver
```
