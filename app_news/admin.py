from django.contrib import admin

from .models import News, Category


# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'news_title', 'news_date')
    search_fields = ('news_title', 'news_txt')
    # list_filter = ('')


admin.site.register(News, NewsAdmin)
admin.site.register(Category)