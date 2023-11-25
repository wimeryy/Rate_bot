from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
from lexicon.lexicon import LEXICON
from keyboards.builder_keyboards import create_inline_keyboard, keyboard

router = Router()


@router.message(Command(commands='start'))
async def process_command_start(message: Message):
    await message.answer(LEXICON['/start'])


@router.message(Command(commands='help'))
async def process_command_help(message: Message):
    await message.answer(LEXICON['/help'])


@router.message(Command(commands='crypto'))
async def process_command_crypto(message: Message):
    await message.answer(text='f', reply_markup=keyboard)


@router.message(Command(commands='currency'))
async def process_command_currency(message: Message):
    pass


@router.message()
async def send_echo(message: Message):
    await message.answer(f'Неизвестная команда. Ваше сообщение: {message.text}')