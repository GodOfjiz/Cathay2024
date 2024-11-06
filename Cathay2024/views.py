from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import Activity, Route, Tickets
import json

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Welcome to API HELL!"})

@api_view(['GET', 'POST'])
def activity_seeking(request):
    if request.method == 'POST':
        location = request.data.get('location', 'Osaka')
        no_of_suggestions = request.data.get('no_of_suggestions', 10)
        activities = Activity.GETactivityloc(destination=location, no_of_suggestions=no_of_suggestions)
        return Response(activities)

@api_view(['GET', 'POST'])
def route_optimize(request):
    if request.method == 'POST':
        destination = request.data.get('destination')
        origin = request.data.get('origin')
        travel_mode = request.data.get('travel_mode', ['TRAIN'])
        route_pref = request.data.get('route_pref')
        answer = Route.POSTroute(destination = destination, origin = origin, travel_mode = travel_mode, route_pref = route_pref, alternative = False)
        return Response(answer)

