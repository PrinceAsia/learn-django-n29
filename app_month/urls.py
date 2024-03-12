from django.urls import path

from .views import month_view

urlpatterns = [
    path('list/', month_view, name='month_list'),
]
