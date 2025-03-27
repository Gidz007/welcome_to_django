from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    # a context is a part of building your html.
    # it is called jinja. 
    date = 2025
    name = "Refactory Academy CSE Python Class"
    ground_breakers = 50
    refactory_students = 60
    others = 80
    total = ground_breakers + refactory_students + others
    context = {
        "class_name": name,
        "total_students" : total,
        "date" : date
    }
    return render(request, "index.html", context)

def aboutpage(request):
    return render(request, "about.html" )

def contactpage(request):
    return render(request, "contacts.html")

def mepage(request):
    context = {
        "owner_name" : "Gideon", 
    }
    return render(request, "me.html", context)