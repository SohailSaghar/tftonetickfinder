from lcu_driver import Connector
import pprint

connector = Connector()


# GET /lol-ranked/v1/league-ladders/{puuid} når jeg får en master+ acc.
# 9da29aab-8792-5311-930c-71b72a996199 master puuid
# 38b675bc-39ca-50b2-8da0-c7f72f13c776 rank 1 master -> GM
# 4127b174-2a10-592c-a866-5ef7f953c7bd rank 1 GM -> chall
# kan nok bare lavet lortet kun for euw.
# basically vi har for rank 1 masters, så kan vi bare vente til at han kommer i GM, så nakker vi dem og så
# kan vi få challenger efter at se på førstes.

@connector.ready
async def connect(connection):
    summoner = await connection.request('get', '/lol-ranked/v1/league-ladders/38b675bc-39ca-50b2-8da0-c7f72f13c776')
    # pprint.pp(await summoner.json())

    hej = await summoner.json()
    with open("gm.txt", "w", encoding="utf-8") as file:
        file.write(str(hej))


connector.start()
