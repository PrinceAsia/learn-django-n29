from django.shortcuts import render
from django.http import HttpResponse

from config.settings import BASE_DIR


links = f""


# Create your views here.
def index(request):
    with open(BASE_DIR / 'app_pages/my_file.txt', 'r') as file:
        lines = file
        for line in lines:
            print(line)
    return render(request, "index.html")
    # return HttpResponse("<h1>Index page</h1>" + links)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
