# Django

- [Django Install](#djnago-install)
- [Django Structure](#djnago-structure)
- [Django MTV](./django-mtv.md)



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


# 프로젝트 생성
$ django-admin startproject [프로젝트]

# 앱 생성
$ python manage.py startapp [앱]

# 모델 변경 사항 추적
$ python manage.py makemigrations

# 디비 생성 및 변경 사항 반영
$ python manage.py migrate

## 테이블이 생성되지 않을 경우
$ python manage.py migrate --fake [앱] zero


# 관리자 생성
$ python manage.py createsuperuser

# 관리자 비밀번호 변경
$ python manage.py changepassword


# 서버 실행
$ python manage.py runserver


# 테스트 실행
$ python manage.py test
$ python manage.py test -v 3
```


## Django Structure

```bash
project/
├── project_app/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── test.py
│   └── views.py
├── project_server/
│   ├── asgi.py        
│   ├── settings.py  
│   ├── urls.py        
│   └── wsgi.py        
├── manage.py          
└── requirements.txt   
```


\+ ASGI    
https://github.com/yoojj/Python/blob/master/wsgi.md#asgi



### settings  
https://docs.djangoproject.com/en/3.0/ref/settings/

**database**   
- django.db.backends.sqlite3
- django.db.backends.mysql
- django.db.backends.postgresql_psycopg2
- django.db.backends.oracle
- ...



[top](#)
