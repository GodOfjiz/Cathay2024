from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
from .models import Package
# Create your views here.

def APIgen(request):
    # packages names,location, activities, intermodal services
    context = {
        'Travel_Planner': Package.objects.all()
    }
    answer = {

    }
    queryset = Package.objects.all()
    data = list(queryset.values())
    return JsonResponse(data, safe=False)
=======
from .models import Packages
# Create your views here.

def APIgeneration(request):
    # packages names,location, activities, intermodal services
    context = {
        'Travel_Planner': Packages.objects.all()
    }
    return render(request,"RemoteDatabase/xxx.html", context)
>>>>>>> main
