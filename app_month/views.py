from django.shortcuts import render


# Create your views here.
def month_view(request):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return render(request, 'months/months_list.html', {'oylar': months})