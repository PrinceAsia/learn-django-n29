from django.shortcuts import render

months = [
    ('January', 31),
    ('February', 28),
    ('March', 31)
]


# Create your views here.
def month_view(request):
    return render(request, 'months/months_list.html', {'oylar': months})


def month_days(request, pk):
    return render(request, 'months/month_view.html', {'oy': months[pk]})
