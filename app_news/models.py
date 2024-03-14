from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Category Name')
    description = models.CharField(max_length=255, blank=True, verbose_name='Description')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']
        db_table = 'categories'


class News(models.Model):
    news_title = models.CharField(max_length=255, verbose_name='News title')
    news_txt = models.TextField(verbose_name='News content')
    news_date = models.DateTimeField(verbose_name='News inserted time', auto_now_add=True)
    news_category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='', null=True)
    views_count = models.IntegerField(verbose_name='Views count', default=0)

    def __str__(self):
        return f"{self.pk}. {self.news_title}"

    class Meta:
        verbose_name = 'News'
        db_table = 'news' # app_news_news
        verbose_name_plural = 'News'
        ordering = ['id']
