import asyncio
import logging

from aiogram import Bot, Dispatcher
from config.config import Config, load_config
from keyboards.main_menu import set_main_menu
from handlers import callback_handlers, message_handlers

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')

    config: Config = load_config()

    bot = Bot(token=config.Rate_bot.token,
              parse_mode='HTML')
    dp = Dispatcher()

    await set_main_menu(bot)

    dp.include_router(message_handlers.router)
    dp.include_router(callback_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
