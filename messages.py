from api_service import get_weather
from coordinates import get_coordinates


def weather() -> str:
    """Returns a message about the temperature and weather description"""
    wthr = get_weather(get_coordinates())
    return (
        f"{wthr.location}, {wthr.description}\n"
        f"Temperature is {round(wthr.temperature, 0)}°C, feels like {round(wthr.temperature_feeling, 0)}°C"
    )


def wind() -> str:
    """Returns a message about wind direction and speed"""
    wthr = get_weather(get_coordinates())
    return f"{wthr.wind_direction} wind {wthr.wind_speed} m/s"


def sun_time() -> str:
    """Returns a message about the time of sunrise and sunset"""
    wthr = get_weather(get_coordinates())
    return (
        f'Sunrise: {wthr.sunrise.strftime("%H:%M")}\n'
        f'Sunset: {wthr.sunset.strftime("%H:%M")}\n'
    )
