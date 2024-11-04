from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
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
