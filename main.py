import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import Message, ContentTypes
from aiogram.utils import executor

from config import TOKEN

logging.basicConfig(level=logging.DEBUG)

bot = Bot(TOKEN)
dp = Dispatcher(bot)

logging_middleware = LoggingMiddleware()
dp.middleware.setup(logging_middleware)


@dp.message_handler()
async def echo_message(message: Message):
    return await message.answer(message.text)
    # await bot.send_message()


@dp.message_handler(content_types=ContentTypes.PHOTO)
async def echo_photo(message: Message):
    return await message.answer_photo(
        message.photo[-1].file_id,
        caption=f"You wrote: {message.caption!r}",
    )


@dp.message_handler(content_types=ContentTypes.STICKER | ContentTypes.ANIMATION)
async def forward_any_sticker(message: Message):
    return await message.forward(message.chat.id)

if __name__ == '__main__':
    executor.start_polling(dp)
