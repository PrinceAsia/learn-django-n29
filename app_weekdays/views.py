from django.shortcuts import render


week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


# Create your views here.
def weekdays(request):
    return render(request, 'weekdays/days.html', {'hafta': week})
