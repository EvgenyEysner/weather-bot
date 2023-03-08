import json
from dataclasses import dataclass
from urllib.request import urlopen


@dataclass(frozen=True)
class Coordinates:
    longitude: float
    latitude: float


def get_coordinates() -> Coordinates:
    """
    Returns current coordinates using IP address
    """
    data = _get_ip_data()
    latitude = data["loc"].split(",")[0]
    longitude = data["loc"].split(",")[1]

    return Coordinates(latitude=latitude, longitude=longitude)


# You can find them by IP address using ipinfo.io/json.
def _get_ip_data() -> dict:
    """
    This is the response.
    {
      "ip": "228.228.228.228",
      "city": "Moscow",
      "region": "Moscow",
      "country": "RU",
      "loc": "55.7522,37.6156",
      "org": "Starlink",
      "postal": "101000",
      "timezone": "Europe/Berlin",
      "readme": "https://ipinfo.io/missingauth"
    }
    """
    url = "http://ipinfo.io/json"
    response = urlopen(url)
    return json.load(response)
