import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()
 
url = "https://v3.football.api-sports.io/"
api_key = os.getenv('rapidapi_key')

payload = {}
headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': 'v3.football.api-sports.io'
}

def get_league(id):
    league_url = url +'leagues'
    file_name = 'league_' + id
    response = requests.request("GET", league_url, headers=headers, data=payload, params={'id':id})
    json_data = str(response.text)
    json_data = json_data.replace('\"', '"')

    with open(file_name + ".json", 'w') as outfile:
        json.dump(json_data, outfile)

