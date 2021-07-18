from django.http.response import HttpResponse
from django.shortcuts import render
from . models import Skill
from django.core.mail import send_mail
from django.conf import settings 

# Create your views here.
def index(request):
    
    if request.method == "POST":
        email = request.POST[ 'email']
        message = request.POST['message']
        fullname = request.POST['fullname']
        send_mail(
    'test',
    message,
    settings.EMAIL_HOST_USER,
    [email],
    fail_silently = False,
)
    
    skills = Skill.objects.all()
    context = {'skills': skills}
    return render(request, 'index.html',context)