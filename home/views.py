from django.shortcuts import render

# Create your views here.

# The homepage function.
def homepage(request):
    # a context is a part of building your html.
    # it is called jinja templating.
    date = 2025
    name = "Refactory Academy CSE Python Class"
    ground_breakers = 50
    refactory_students = 60
    others = 80
    total = ground_breakers + refactory_students + others
    context = {
        "class_name": name,
        "total_students" : total,
        "date" : date,
    }
    return render(request, "index.html", context)

# The aboutpage function.
def aboutpage(request):
    return render(request, "about.html" )

# The contactpage fuction.
# Using a context as a dictionary having keys to make changes on my Html page,
def contactpage(request):
    reaction = "He is not going to school, he is .."
    context = {
        "health" : reaction,
        "numbers" : 2025
    }
    return render(request, "contacts.html", context)

def productspage(request):
    return render(request, "products.html")

# Leadership page.
def leadershipage(request):
    return render(request, "leadership.html")

# The studets list page.
def studentspage(request):
    return render(request, "students/allstudents.html")

# Viewing a student's details.
def viewstudents(request, student_name):
    return render(request, "students/viewstudents.html")