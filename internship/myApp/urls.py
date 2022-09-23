from django.urls import path, include
from . import views


app_name = 'myApp'

urlpatterns = [
    path('', views.index, name='index')
]
