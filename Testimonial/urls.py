from django.urls import path
from . import views

app_name = 'Testimonial'

urlpatterns = [
    path('', views.index, name='index'),
]
