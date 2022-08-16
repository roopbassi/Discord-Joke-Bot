import requests
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()
configure()

url = "https://dad-jokes.p.rapidapi.com/random/joke"
headers = {
	"X-RapidAPI-Key": f"{os.getenv('api_key')}",
	"X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
}

def get_joke():
    response = requests.request("GET", url, headers=headers)
    setup = response.json()['body'][0]['setup']
    punchline = response.json()['body'][0]['punchline']
    return setup + " " + punchline

get_joke()
