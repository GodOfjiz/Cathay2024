from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import Activity, Route, Tickets, ollama_chatbot
import json

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Welcome to API HELL!"})

@api_view(['GET', 'POST'])
def activity_seeking(request):
    if request.method == 'POST':
        key = list(request.data.keys())[0]
        location = request.data[key]
        key2 = list(request.data.keys())[1]
        suggestions = request.data[key2]
        no_of_suggestions = request.data.get('no_of_suggestions', '10')
        
        activities = Activity.GETactivityloc(destination=location, no_of_suggestions=suggestions)
        return Response(activities)

@api_view(['GET', 'POST'])
def route_optimize(request):
    if request.method == 'POST':
        destination = request.data.get('destination')
        origin = request.data.get('origin')
        travel_mode = request.data.get('travel_mode', ['TRAIN'])
        route_pref = request.data.get('route_pref', 'LESS_WALKING')
        answer = Route.POSTroute(destination = destination, origin = origin, travel_mode = travel_mode, route_pref = route_pref, alternative = False)
        return Response(answer)

@api_view(['GET','POST'])
def chatbotting(request):
    if request.method == 'POST':
        key = list(request.data.keys())[0]
        question = request.data[key]
    elif request.method == 'GET':
        question = "Who are you?"
    text = ollama_chatbot.chatbot(question)
    return Response(text)
    
