from typing import NamedTuple
from geopy import Nominatim
from geopy.location import Location
# from dataclasses import dataclass

from exceptions import CantGetCoordinates
import config


#NamedTuple - именованный картеж
class Coordinates(NamedTuple):
    latitude: float
    longitude: float

def get_gps_coordinates() -> Coordinates:
    """return current coordinates using package GeoPy"""
    coordinates = _get_coordinates()
    return _round_coordinates(coordinates)

#Модули с _, используются только для этого файла
def _get_coordinates() -> Coordinates:
    locale = _get_currect_locale()
    return Coordinates(
        latitude=locale.latitude,
        longitude=locale.longitude,
    )

def _get_currect_locale() -> Location:
    locale = _get_locale()
    if locale is None:
        raise CantGetCoordinates
    return locale

def _get_locale() -> Location:
    # addres = _get_addres()
    addres = config.ADDRES
    geolocator = Nominatim(user_agent="run")
    locale = geolocator.geocode(addres)
    return locale

# def _get_addres():
#     addres = input()
#     #Свои проверки
#     return addres

def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    if not config.USE_ROUNDED_COORDS:
        return coordinates
    return Coordinates(*map(lambda x: round(x, 1),[
        coordinates.latitude,
        coordinates.longitude
    ]))

if __name__ == '__main__':
    print(get_gps_coordinates())

# coordinates = get_gps_coordinates()
# print(coordinates.latitude, coordinates.longitude)


# @dataclasse
# class Coordinates:
#     longitude: float
#     latitude: float
# def get_gps_coordinates() -> Coordinates:
#     # return Coordinates(**{"latitude": 20, "longitude": 30})
#     return Coordinates(latitude=20, longitude=30)
#
# coordinates = get_gps_coordinates()
# print(coordinates.latitude, coordinates.longitude)


#TypedDict - типизированный словарь
# class Coordinates(TypedDict):
#     longitude: float
#     latitude: float
# def get_gps_coordinates() -> Coordinates:
#     return Coordinates(**{"latitude": 20, "longitude": 30})
#
# coordinates = get_gps_coordinates()
# print(coordinates['latitude'], coordinates['longitude'])
