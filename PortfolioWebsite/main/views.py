from django.http.response import HttpResponse
from django.shortcuts import render
from . models import Skill

# Create your views here.
def index(request):
    skills = Skill.objects.all()
    context = {'skills': skills}
    return render(request, 'index.html',context)