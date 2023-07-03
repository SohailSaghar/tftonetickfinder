import requests
import pprint
pp = pprint.PrettyPrinter(indent=4)
headers = {
    # api key. needs to be refreshed every 24 hrs.
    'X-Riot-Token': ''
}

url = "https://europe.api.riotgames.com/tft/match/v1/matches/EUW1_6469287071"
response = requests.request("GET", url, headers=headers)
pp.pprint(response.json()["info"]["participants"][2]["placement"])