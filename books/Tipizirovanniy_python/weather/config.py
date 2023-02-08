USE_ROUNDED_COORDS = True
OPEN_WEATHER_API = "8579956c8e46511b1523cc70f45531c2"
ADDRES = "New York"

#OpenWeather
#"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}"

OPEN_WEATHER_URL = (
    "https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current_weather=true&temperature_unit=celsius&timeformat=unixtime"
)
WEATHER_CODES = {
    "0": "Clear",
    "1": "Clear",
    "2": "Cloudy",
    "3": "Overcast",

    "45": "Fog",
    "48": "Fog",

    "51": "Drizzle",
    "53": "Drizzle",
    "55": "Drizzle",

    "56": "Freezing Drizzle",
    "57": "Freezing Drizzle",

    "61": "Rain",
    "63": "Rain",
    "65": "Rain",

    "66": "Freezing Rain",
    "67": "Freezing Rain",

    "71": "Snow fall",
    "73": "Snow fall",
    "75": "Snow fall",

    "77": "Snow grains",

    "80": "Rain showers",
    "81": "Rain showers",
    "82": "Rain showers",

    "85": "Snow showers",
    "86": "Snow showers",

    "95": "Thunderstorm",
    "96": "Thunderstorm",
    "99": "Thunderstorm"
}