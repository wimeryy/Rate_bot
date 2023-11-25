import asyncio
import logging

from aiogram import Bot, Dispatcher
from config.config import Config, load_config
from keyboards.main_menu import set_main_menu
from handlers import callback_handlers, message_handlers
