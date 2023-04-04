### Description
    Python 3.8
A simple Telegram Weather Bot.
### Virtual environment

To avoid conflicting interpreters and package versions it is recommended to
[use a virtual environment](https://code.visualstudio.com/docs/python/tutorial-django#_create-a-project-environment-for-the-django-tutorial)

```bash
python3 -m venv .venv
```

```bash
. .venv/bin/activate
```

### Install Dependencies
```bash
pip install pipenv
```

```bash
pipenv install
```

### Create New Bot by BotFather:
    https://botostore.com/c/botfather/

### Create .env file in root directory
```bash
touch .env
```

### and dds the following entries from the Telegram API

    WEATHER_API_KEY=YOUR APIKEY FROM https://openweathermap.org/
    BOT_API_TOKEN=BOT_API_TOKEN FROM BOtFather

### Run App
```bash
python3 bot.py
```