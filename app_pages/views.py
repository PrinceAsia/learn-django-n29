from django.shortcuts import render
from django.http import HttpResponse


links = f""


# Create your views here.
def index(request):
    return render(request, "index.html")
    # return HttpResponse("<h1>Index page</h1>" + links)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
