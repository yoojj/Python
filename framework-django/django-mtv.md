# Django MTV Pattern

```
request --> url --> view <--> model
response    <--     view <--> template
```


## Url
https://docs.djangoproject.com/en/3.0/ref/urls/

```python
from django.urls import path, re_path, include

urlpatterns = patterns('',
    path('', include('django_app.urls')),
    re_path(r'^', include('django_app.urls')),
)
```



## View
https://docs.djangoproject.com/en/3.0/ref/class-based-views/

```python
# views.py
from django.views import View
from django.http import HttpResponse

class TestView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse()


# urls.py
urlpatterns = [
    path('/', TestView.as_view(), name='test'),
]
```


**django rest**   
https://www.django-rest-framework.org/api-guide/views/

```python
# views.py
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

@api_view(['GET'])
def get_test(request, param=None):
    return Response()

class TestView(APIView):
    def get(self, request, param=None):
        return Response()
```



## Model
https://docs.djangoproject.com/en/3.0/ref/models/

```python
# models.py
from django.db import models

class TestModel(models.Model):
    pk = models.AutoField(primary_key=True)
    int_32 = IntegerField()
    int_64 = BigIntegerField()
    varchar = models.CharField(max_length=10)
    text = models.TextField()

    class Meta:
        db_table = 'table_name'


# views.py
def test():
    # insert
    object = TestModel(varchar = '')
    object.save()

    # select
    object = TestModel.objects.all()
    object = TestModel.objects.get(pk = 1)

    # update
    object = TestModel.objects.get(pk = 1)
    object.key = ''
    object.save()

    # delete
    object = TestModel.objects.get(pk = 1)
    object.delete()
```


### Model Relationship   

- OneToOneField
- ForeignKey
- ManyToManyField


**OneToOneField vs ForeignKey(unique=True)**   



## Template
https://docs.djangoproject.com/en/3.0/ref/templates/

```python
from django.shortcuts import render, redirect

def render_test(request):
    return render(request, 'test.html', { 'key' : 'value' })

def redirect_test(request):
    return redirect('')
```

**DTL**  
Django Template Language  
https://docs.djangoproject.com/en/3.1/ref/templates/language/  

```html
{# 주석 #}
{% comment %}
주석
{% endcomment %}

<!-- 변수 -->
<h1>{{ title }}</h1>
<p>{{ object.key }}</p>

<!-- 내장 필터 -->
<p>{{ text | length }}</p>
<p>{{ text | truncatewords:10 }}</p>

<!-- 태그 -->
<ul>
{% for i in list %}
    <li>{% i.key %}</li>
{% endfor %}
</ul>
```


[top](#)
