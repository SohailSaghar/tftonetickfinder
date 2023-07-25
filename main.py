import multiprocessing
from onetricks.searching_for_one_trick import asia_finder, america_finder, europe_finder, sea_finder
from onetricks.master_plus_puuids import request_summoner_id, summoner_id_to_puuid, save_to_db


if __name__ == '__main__':
    """
    servers = ["br1", "eun1", "euw1", "jp1", "kr",
               "la1", "la2", "na1", "oc1", "ph2",
               "ru", "sg2", "th2", "tr1", "tw2", "vn2"
               ]
    leagues = ["grandmaster", "challenger"]

    for server in servers:
        for league in leagues:
            summoner_ids = request_summoner_id(server, league)
            puuids = summoner_id_to_puuid(server, summoner_ids)
            save_to_db(server, league, puuids)
    """

    asia = multiprocessing.Process(target=asia_finder)
    america = multiprocessing.Process(target=america_finder)
    europe = multiprocessing.Process(target=europe_finder)
    sea = multiprocessing.Process(target=sea_finder)
    print("asia start")
    asia.start()
    print("america start")
    america.start()
    print("europe start")
    europe.start()
    print("sea start")
    sea.start()
    print("all processes are started")

    asia.join()
    america.join()
    europe.join()
    sea.join()


