from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    token: str
    api_key: str

@dataclass
class Config:
    Weather_bot: TgBot

def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(Weather_bot=TgBot(token=env('BOT_TOKEN'),
                                    api_key=env('API_KEY')))