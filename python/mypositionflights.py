
import geocoder
from FlightRadar24 import FlightRadar24API
fr_api = FlightRadar24API()

# my GPS position
def get_current_gps_coordinates():
    g = geocoder.ip('me')#this function is used to find the current information using our IP Add
    if g.latlng is not None: #g.latlng tells if the coordiates are found or not
        return g.latlng
    else:
        return None

if __name__ == "__main__":
    coordinates = get_current_gps_coordinates()
    if coordinates is not None:
        latitude, longitude = coordinates
        print(f"Your current GPS coordinates are:")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
    else:
        print("Unable to retrieve your GPS coordinates.")

bounds = fr_api.get_bounds_by_point(latitude, longitude, 2000)
flights = fr_api.get_flights(bounds = bounds)
print (flights)