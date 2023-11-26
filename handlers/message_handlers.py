from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
from lexicon.lexicon import LEXICON
from keyboards.builder_keyboards import create_inline_keyboard
from services.services import get_bitcoin_to_usd_price, get_ethereum_to_usd_price, get_usd_to_rub_exchange_rate

router = Router()


@router.message(Command(commands='start'))
async def process_command_start(message: Message):
    await message.answer(LEXICON['/start'])


@router.message(Command(commands='help'))
async def process_command_help(message: Message):
    await message.answer(LEXICON['/help'])


@router.message(Command(commands='btc'))
async def process_command_btc(message: Message):
    price = get_bitcoin_to_usd_price()
    await message.answer(f"{LEXICON['/btc']} {price} ₿")


@router.message(Command(commands='eth'))
async def process_command_eth(message: Message):
    price = get_ethereum_to_usd_price()
    await message.answer(f"{LEXICON['/eth']} {price} 🌐")


@router.message(Command(commands='usd'))
async def process_command_usd(message: Message):
    price = get_usd_to_rub_exchange_rate()
    await message.answer(f"{LEXICON['/usd']} {price} 💲")


@router.message()
async def send_echo(message: Message):
    await message.answer(f'Неизвестная команда. Ваше сообщение: {message.text}')
