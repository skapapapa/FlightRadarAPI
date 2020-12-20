# FlightRadarAPI
API for [Flight Radar 24](https://www.flightradar24.com/) written in Python 3.

[![Python Package](https://github.com/JeanExtreme002/FlightRadarAPI/workflows/Python%20Package/badge.svg)](https://github.com/JeanExtreme002/FlightRadarAPI/actions)
[![Pypi](https://img.shields.io/pypi/v/FlightRadarAPI)](https://pypi.org/project/FlightRadarAPI/)
[![License](https://img.shields.io/pypi/l/FlightRadarAPI)](https://pypi.org/project/FlightRadarAPI/)
[![Python Version](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue)](https://pypi.org/project/FlightRadarAPI/)

# Installing FlightRadarAPI:
```
pip3 install FlightRadarAPI
```

# Basic Usage:
Just create a `FlightRadar24API` object after importing it.

```
from FlightRadar24.api import FlightRadar24API
fr_api = FlightRadar24API()
```

**Getting airports list:**
```
airports = fr_api.get_airports()
```

**Getting airlines list:**
```
airlines = fr_api.get_airlines()
```

**Getting flights list:**
```
flights = fr_api.get_flights()
```

**Getting zones list:**
```
zones = fr_api.get_zones()
```

You can also get more information about a specific flight such as: aircraft images, estimated time, trail, etc.
```
f_details = fr_api.get_flight_details(flight.flight_id)

flight.set_flight_details(f_details)
print("Flying to", flight.destination_airport_info["name"])
```

# Filtering flights and airports:
**Getting flights by airline:**
```
airline_icao = "AZU"
thy_flights = fr_api.get_flights(airline = airline_icao)
```

**Getting flights by bounds:**
```
bounds = fr_api.get_bounds(zone)
flights = fr_api.get_flights(bounds = bounds)
```

**Getting airports by ICAO:**
```
icao = "VNLK"
lukla_airport = fr_api.get_airport(icao = icao)
```

**Getting airports by IATA:**
```
iata = "LUA"
lukla_airport = fr_api.get_airport(iata = iata)
```

**Getting and configuring Real-time Flight Tracker parameters:**
```
params = fr_api.get_real_time_flight_tracker_config()
set_real_time_flight_tracker_config(new_config)
```
