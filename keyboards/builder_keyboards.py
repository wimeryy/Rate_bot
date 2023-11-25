from lexicon.lexicon import LEXICON
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def create_inline_keyboard(*buttons: str) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(*[InlineKeyboardButton(
        text=LEXICON[button] if button in LEXICON else button,
        callback_data=button) for button in buttons]
    )
    return kb_builder.as_markup()


kb_builder = ReplyKeyboardBuilder()

BTC_btn = KeyboardButton(
    text=LEXICON['BTC'],
)

ETH_btn = KeyboardButton(
    text=LEXICON['ETH'],
)

kb_builder.row(BTC_btn, ETH_btn, width=1)
keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)
