from django.urls import path, include
from django_app import views

urlpatterns = [
    path('get', views.get, name='get-test'),
    path('get/<param>', views.get, name='get-test'),
    path('post', views.post, name='post-test'),
]
