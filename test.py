import requests
import pprint
headers = {
    # api key. needs to be refreshed every 24 hrs.
    'X-Riot-Token': ''
}

match = "EUW1_6503202232"

url = f"https://europe.api.riotgames.com/tft/match/v1/matches/{match}"
response = requests.request("GET", url, headers=headers)
print(int(response.json()["info"]["game_version"].split(" ")[1].split(".")[0]) == 13)

# pprint.pp(response.json()["info"]["participants"])

pprint.pp(response.json()["info"]["participants"][2]["augments"])
