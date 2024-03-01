from django.shortcuts import render
from aa.models import Course
# Create your views here.


def home(req):
    context = {
        'course': Course.objects.all()
    }
    return render(req, 'home.html',context)