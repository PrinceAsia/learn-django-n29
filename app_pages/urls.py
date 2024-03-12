from django.urls import path

from .views import index, about, contact


urlpatterns = [
    path('about/', about, name='about_url'),
    path('contact/', contact, name='contact_url'),
    path('', index, name='index_url'),
    path('index/', index, name='index_url'),
]
