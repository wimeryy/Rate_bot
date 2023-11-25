import requests
from config.config import Config, load_config

config: Config = load_config()

api_key = config.Weather_bot.api_key
