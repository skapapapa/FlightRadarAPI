# https://github.com/JeanExtreme002/FlightRadarAPI/blob/main/python/README.md

import json
import time
from FlightRadar24 import FlightRadar24API
fr_api = FlightRadar24API()

# GET SCHIPHOL DETAILS
schiphol_icao = "EHAM"
schiphol_airport = fr_api.get_airport(code = schiphol_icao, details = True)

# EXTRACT SCHIPHOL ARRIVALS
schiphol_arrivals = schiphol_airport.arrivals['data']
arrivals_json = json.dumps(schiphol_arrivals[0], indent=4)
with open("python/data/schipholarrival.json", "w") as outfile:
    outfile.write(arrivals_json)

# EXTRACT SCHIPHOL DEPARTURES
schiphol_departures = schiphol_airport.departures['data']
departures_json = json.dumps(schiphol_departures[0], indent=4)
with open("python/data/schipholdeparture.json", "w") as outfile:
    outfile.write(departures_json)

# FILTER FOR SPECIFIC TIME WINDOWS
ut = time.time()
print(ut)
# 1549281692.9876952


# ENABLE REALTIME BY IMPLEMENTING A POLLING MECHANISM
# (https://pypi.org/project/polling2/)