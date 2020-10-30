# Django

- [Django Install](#djnago-install)
- [Django Structure](#djnago-structure)



## Django Install

```bash
# 가상 환경 생성 및 실행
$ python3.9 -m venv ./ENV
$ source ENV/bin/active

# requirements.txt 파일이 있다면
# $ pip install -r requirements.txt

$ pip install django djangorestframework django-cors-headers django-environ mysql-connector-python
$ django-admin --version

# requirements.txt 생성
$ pip freeze > requirements.txt


# 프로젝트 생성 및 실행 
$ django-admin startproject [프로젝트]
$ python manage.py startapp [app]

$ python manage.py makemigrations [app]
$ python manage.py migrate
$ python manage.py runserver


# test 실행
$ python manage.py test
$ python manage.py test -v 3
```


## Django Structure

```bash
project/
├── project_app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── test.py
│   └── views.py
├── project_server/
│   ├── __init__.py
│   ├── asgi.py        
│   ├── settings.py  
│   ├── urls.py        
│   └── wsgi.py        
├── manage.py          
└── requirements.txt   
```


\+ ASGI    
https://github.com/yoojj/Python/blob/master/wsgi.md#asgi
