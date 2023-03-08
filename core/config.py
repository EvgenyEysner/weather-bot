import os

import environ

env = environ.Env()
# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

BOT_API_TOKEN = env("BOT_API_TOKEN")
WEATHER_API_KEY = env("WEATHER_API_KEY")

CURRENT_WEATHER_API_CALL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + WEATHER_API_KEY + "&units=metric"
)
