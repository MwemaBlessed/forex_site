"""
URL configuration for crypto_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('how-to-do/', include('how_to_do.urls', namespace='how_to_do')),
    path('free/', include('Free.urls', namespace='Free')),
    path('paid/', include('Paid.urls', namespace='Paid')),
    path('Services/', include('Services.urls', namespace='Services')),
    path('Subscription/', include('Subscription.urls', namespace='Subscription')),
    path('Testimonial/', include('Testimonial.urls', namespace='Testimonial')),
    path('about/', include('about.urls', namespace='about')),

]
