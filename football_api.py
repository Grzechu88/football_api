import requests
from dotenv import load_dotenv
import os

load_dotenv()
 
url = "https://v3.football.api-sports.io/"
api_key = os.getenv('rapidapi_key')

payload = {}
headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': 'v3.football.api-sports.io'
}

response = requests.request("GET", url, headers=headers, data=payload, params={'id':339})

print(response.text)