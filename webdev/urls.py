from django.contrib import admin
from django.urls import path, include
from webdev.home_view import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('tarefas/', include('webdev.tarefas.urls'))
]
