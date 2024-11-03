from django.shortcuts import render
from django.http import HttpResponse
from .models import Packages
# Create your views here.

def APIgeneration(request):
    # packages names,location, activities, intermodal services
    context = {
        'Travel_Planner': Packages.objects.all()
    }
    return render(request,"RemoteDatabase/xxx.html", context)
