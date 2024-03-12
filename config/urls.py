from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weekdays/', include('app_weekdays.urls')),
    path('month/', include('app_month.urls')),
    path('', include('app_pages.urls')),
]
