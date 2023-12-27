import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from config import Token
from aiogram.filters import Command
from aiogram.types import FSInputFile
from aiogram.utils.media_group import MediaGroupBuilder

TOKEN = Token

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message(Command("album"))
async def cmd_album(message: types.Message):
    album_builder = MediaGroupBuilder(
        caption="Albumli video uchum Templates"
    )
    album_builder.add(
        type="video",
        media=FSInputFile("test video.mp4"))
    album_builder.add(
        type="video",
        media=FSInputFile("test video.mp4"))
    album_builder.add(
        type="video",
        media=FSInputFile("test video.mp4"))
    album_builder.add(
        type="video",
        media=FSInputFile("test video.mp4"))
    album_builder.add(
        type="photo",
        media=FSInputFile("test video.mp4"))

    await message.answer_media_group(media=album_builder.build())


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
