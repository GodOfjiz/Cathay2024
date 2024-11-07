import requests

def GETdeslatlon(destination):
    des_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={destination}&key=gaeee'
    des_res = requests.get(des_url)
    des_lat = des_res.json()['results'][0]['geometry']['location']['lat']
    des_lon = des_res.json()['results'][0]['geometry']['location']['lng']
    return des_lat, des_lon

def GETactivityloc(destination, no_of_suggestions):
    des_lat = GETdeslatlon(destination)[0]
    des_lon = GETdeslatlon(destination)[1]
    locations_url = f"https://api.opentripmap.com/0.1/en/places/autosuggest?name={destination}&radius=10000&lon={str(des_lon)}&lat={str(des_lat)}&src_geom=wikidata&src_attr=wikidata&kinds=interesting_places%2Cnatural%2Ccultural&rate=3&format=json&props=base&limit={str(no_of_suggestions)}&apikey=5ae2e3f221c38a28845f05b6628727068eb707c586acd059ef3fcf53"
    locations_headers = {
        "accept": "application/json"
    }

    locations_response = requests.get(locations_url, headers=locations_headers)
    locations = locations_response.json()
    
    def fetch_wikidata(params_id):
        url = 'https://www.wikidata.org/w/api.php'
        try:
            params = {
            'action': 'wbgetentities',
            'ids': params_id, 
            'format': 'json',
            'languages': 'en'
            }
            return requests.get(url, params=params).json()
        except:
            return 'There was an error'
    
    activity = {}
    for i in range(len(locations)):
        name = locations[i]['name']
        des_id = locations[i]['xid']
        des_json = fetch_wikidata(des_id)
        try:
            des = des_json['entities'][des_id]['descriptions']['en']['value']
        except:
            des = 'Not Provided'
        activity[i] = [name, des]

    return activity

GETactivityloc(destination = 'Osaka', no_of_suggestions = 10)
