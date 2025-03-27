from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# The homepage function.
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

# The aboutpage function.
def aboutpage(request):
    return render(request, "about.html" )

# The contactpage fuction.
def contactpage(request):
    reaction = "He is not going to school, he is .."
    """Using a context as a dictionary having keys
    to make changes on my Html page, 
    """
    context = {
        "health" : reaction,
        "numbers" : 2025
    }
    return render(request, "contacts.html", context)

# The mepage function.
def mepage(request):
    context = {
        "owner_name" : "Gideon", 
    }
    return render(request, "me.html", context)