from django.shortcuts import render


class learner:
    def __init__(
        self, id_num, first_name, last_name, email, course, passport_photo, gender
    ):
        self.id_num = id_num
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.course = course
        self.passport_photo = passport_photo
        self.gender = gender


# Create your views here.
def learnerspage(request):
    Lilian = learner(
        id_num="1",
        first_name="lillian",
        last_name="nantume",
        email="n.lillian.ac",
        course="PSE",
        passport_photo="h",
        gender="F",
    )
    retisha = learner(
        id_num="2",
        first_name="retisha",
        last_name="agenroth",
        email="n.retisha.ac",
        course="PSE",
        passport_photo="p",
        gender="F",
    )
    mark = learner(
        id_num="3",
        first_name="mark",
        last_name="andrew",
        email="n.latim.ac",
        course="data science",
        passport_photo="j",
        gender="m",
    )
    return render(request, "learners.html")
