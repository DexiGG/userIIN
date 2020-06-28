from django.shortcuts import render
from sqlalchemy.orm.exc import NoResultFound

from .models import Person
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    s = "Hello World остальное вы найдите здесь http://127.0.0.1:8000/person"
    lst = s.split()
    return HttpResponse(lst)


def person(request):
    people = Person.objects.all()
    return render(request, "person.html", {"people": people})


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        uzer = Person()
        uzer.IIN = request.POST.get("IIN")
        uzer.name = request.POST.get("name")
        uzer.surname = request.POST.get("surname")
        uzer.firstname = request.POST.get("firstname")
        uzer.age = request.POST.get("age")
        uzer.save()
    return HttpResponseRedirect("/")