from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str
    api_key_crypto: str
    api_key_currency: str


@dataclass
class Config:
    Rate_bot: TgBot


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(Rate_bot=TgBot(token=env('BOT_TOKEN'),
                                 api_key_crypto=env('API_KEY_CRYPTO'),
                                 api_key_currency=env('API_KEY_CURRENCY')))