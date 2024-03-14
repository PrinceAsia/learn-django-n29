from django.shortcuts import render, get_object_or_404, redirect

from .models import News


# Create your views here.
def news_list(request):
    if 'search' in request.GET:
        news = News.objects.filter(
            news_title__icontains=request.GET['search']
        ) | News.objects.filter(
            news_txt__icontains=request.GET['search'])
        # SELECT * FROM news WHERE news_title LIKE '%keyword%'
    else:
        news = News.objects.all() # SELECT * FROM news;
    return render(request, 'news/news_list.html', {'yangilik': news})


def news_detail(request, pk):
    news = News.objects.get(id=pk)
    # news = get_object_or_404(News, pk)
    # SELECT * FROM news WHERE id=pk;
    return render(request, 'news/news_detail.html', {'news': news})
