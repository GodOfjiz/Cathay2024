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
    if request.method == 'GET':
        data = json.loads(request.body)
        location = data.get('location', 'Osaka')  # Default to 'Osaka' if not provided
        no_of_suggestions = data.get('no_of_suggestions', 10)  # Default to 10 if not provided
        answer = Activity.GETactivityloc(destination = location, no_of_suggestions = no_of_suggestions)
    return Response(answer)

@api_view(['GET', 'POST'])
def route_optimize(request):
    
    answer = Route.POSTroute(destination = 'Rovaniemi', origin = 'GÃ¶teborg Landvetter Airport', travel_mode = ["TRAIN"], route_pref = 'LESS_WALKING', alternative = False)
    return Response(answer)

