import requests
import json
from datetime import datetime

def POSTroute(destination, origin, travel_mode, route_pref, alternative = False):
    route_url = 'https://routes.googleapis.com/directions/v2:computeRoutes'
    route_headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': 'AIzaSyDTpwmj7c2ouLhFE1TU9lA0-5rSKtg1dmw',
        'X-Goog-FieldMask': 'routes.legs.steps.transitDetails'
    }

    route_data = {
        "origin": {
            "address": origin
        },
        #"location": {
            #"address": 'unknown'
        #},
        "destination": {
            "address": destination
        },
        "travelMode": 'TRANSIT',
        "computeAlternativeRoutes": alternative,
        "transitPreferences": {
            "routingPreference": route_pref,
            "allowedTravelModes": travel_mode
        },
    }
    # transfer to JSON str
    route_data = json.dumps(route_data)
    response = requests.post(route_url, headers=route_headers, data=route_data)
    route_res = response.json()
    transit = route_res['routes'][0]['legs'][0]['steps']
    filtered_transit = [step for step in transit if step != {}]
    transit_route = {}
    # Extracting stops and calculating durations
    for route in filtered_transit:
        transit_details = route['transitDetails']

        # Extract arrival and departure stops
        arrival_stop = transit_details['stopDetails']['arrivalStop']['name']
        departure_stop = transit_details['stopDetails']['departureStop']['name']

        # Extract arrival and departure times
        arrival_time_str = transit_details['stopDetails']['arrivalTime']
        departure_time_str = transit_details['stopDetails']['departureTime']

        # Convert to datetime objects
        arrival_time = datetime.fromisoformat(arrival_time_str[:-1])  # Remove 'Z' for UTC
        departure_time = datetime.fromisoformat(departure_time_str[:-1])  # Remove 'Z' for UTC

        # Calculate duration
        duration_timedelta = arrival_time - departure_time
        duration_hours, remainder = divmod(duration_timedelta.total_seconds(), 3600)
        duration_minutes, _ = divmod(remainder, 60)

        # Format duration as a string
        duration_formatted = f"{int(duration_hours)} hours, {int(duration_minutes)} minutes"

        # Get transport agencies
        agencies = transit_details['transitLine']['agencies'][0]['name']
        #agencies_phone = transit_details['transitLine']['agencies'][0].get('phoneNumber', )
        agencies_url = transit_details['transitLine']['agencies'][0]['uri']

        # Get Transport type
        transport = transit_details['transitLine']['vehicle']['type']

        # Store in transit_route dictionary
        transit_route[filtered_transit.index(route)] = [departure_stop, arrival_stop, duration_formatted, 
                                                        agencies, agencies_url, transport]

    # return the transit_route dictionary
    
    return(transit_route)

POSTroute(destination = 'Hong Kong', origin = 'Hong Kong International Airport', travel_mode = ["TRAIN"],
          route_pref = 'LESS_WALKING', alternative = False)

    
