from django.urls import path

from .views import month_view, month_days

urlpatterns = [
    path('<int:pk>/', month_days, name='month_view'),
    path('list/', month_view, name='month_list'),
]
