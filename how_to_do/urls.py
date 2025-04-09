from django.urls import path
from . import views

app_name = 'how_to_do'

urlpatterns = [
    path('', views.index, name='index'),
]
