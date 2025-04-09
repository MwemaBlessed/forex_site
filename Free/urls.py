from django.urls import path
from . import views

app_name = 'Free'

urlpatterns = [
    path('', views.index, name='index'),
]
