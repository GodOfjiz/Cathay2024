from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import Activity, Route, Tickets

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Welcome to API HELL!"})

@api_view(['GET', 'POST'])
def activity_seeking(request):
    answer = Activity.GETactivityloc(destination = 'Osaka', no_of_suggestions = 10)
    return Response(answer)

@api_view(['GET', 'POST'])
def route_optimize(request):
    answer = Route.POSTroute(destination = 'Rovaniemi', origin = 'GÃ¶teborg Landvetter Airport', travel_mode = ["TRAIN"], route_pref = 'LESS_WALKING', alternative = False)
    return Response(answer)


