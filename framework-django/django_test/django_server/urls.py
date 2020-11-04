from django.contrib import admin
from django.urls import path, include


urlpatterns = (
    path('admin/', admin.site.urls),
    path('', include('django_app.urls')),
    path('board/', include('django_app.app_board.urls')),
)
