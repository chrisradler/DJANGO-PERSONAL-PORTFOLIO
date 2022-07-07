from django.shortcuts import render
from .models import Project


def home(request):
    #grab all of the objects from the database in the projects section
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})



