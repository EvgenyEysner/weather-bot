# 🌤️ Telegram Weather Bot

[![Python](https://img.shields.io/badge/python-v3.8-blue)](https://www.python.org/downloads/release/python-380/)
[![Aiogram](https://img.shields.io/badge/aiogram-2.25.1-blue)](https://docs.aiogram.dev/en/latest/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Telegram bot that shows current weather information based on your IP address location.

## ✨ Features

- 🌡️ Current temperature and weather description
- 💨 Wind speed and direction
- 🌅 Sunrise and sunset times
- 📍 Automatic location detection via IP

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Pipenv
- Telegram Bot Token (from [@BotFather](https://t.me/botfather))
- OpenWeather API Key (from [OpenWeather](https://openweathermap.org/))

### Installation

1. Create and activate virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install pipenv
pipenv install
```

3. Create `.env` file in root directory:

```bash
touch .env
```

4. Add required API keys to `.env`:

```
WEATHER_API_KEY=your_openweather_api_key
BOT_API_TOKEN=your_telegram_bot_token
```

### Running the Bot

```bash
python3 bot.py
```

## 📝 Usage

The bot supports following commands:

- `/start` or `/weather` - Show current weather
- `/wind` - Show wind information
- `/sun_time` - Show sunrise/sunset times
- `/help` - Show help message

## 🛠️ Built With

- [aiogram](https://github.com/aiogram/aiogram) - Telegram Bot framework
- [OpenWeather API](https://openweathermap.org/api) - Weather data provider
- [ipinfo.io](https://ipinfo.io/) - IP geolocation service
