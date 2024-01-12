# https://github.com/JeanExtreme002/FlightRadarAPI/blob/main/python/README.md

import inspect
import json
from FlightRadar24 import FlightRadar24API
fr_api = FlightRadar24API()

## inspect a function
# sig = inspect.signature(fr_api.get_flights)
# print(sig)


### schiphol arrivals and departures
# get schiphol details
schiphol_icao = "EHAM"
schiphol_airport = fr_api.get_airport(code = schiphol_icao, details = True)

schiphol_arrivals = schiphol_airport.arrivals['data']
print (schiphol_arrivals[0])
# arrivals_json = json.dumps(schiphol_arrivals)
# arrivals_json = json.loads(arrivals_json)
schiphol_departures = schiphol_airport.departures['data']
print (schiphol_departures[0])


# next step: filter for specific time (see linux time attribute)

# next step: make it realtime by implementing a polling mechanism (https://pypi.org/project/polling2/)


