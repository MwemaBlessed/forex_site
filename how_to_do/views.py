from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Guide

def index(request):
    guides = Guide.objects.all()
    return render(request, 'how_to_do/index.html', {'guides': guides})
