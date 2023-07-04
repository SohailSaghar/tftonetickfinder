import requests
import pprint
from datetime import datetime


pp = pprint.PrettyPrinter(indent=4)
headers = {
    # api key. needs to be refreshed every 24 hrs.
    'X-Riot-Token': ''
}

url = "https://europe.api.riotgames.com/tft/match/v1/matches/EUW1_6469287071"
response = requests.request("GET", url, headers=headers)
pp.pprint(response.json()["info"]["game_version"][65:70])



# String representing the datetime
datetime_str = "Jun 28 2023/03:11:33"

# Convert the string to a datetime object
dt = datetime.strptime(datetime_str, "%b %d %Y/%H:%M:%S")
print(dt.day)

print(dt)
