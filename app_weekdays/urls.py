from django.urls import path

from .views import weekdays

urlpatterns = [
    path('', weekdays, name='weekdays')
]
