from django.urls import path
from . import views

app_name = 'Subscription'

urlpatterns = [
    path('', views.index, name='index'),
]
