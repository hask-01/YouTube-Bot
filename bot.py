import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command

from database import *
from btn import *
from config import *
from utils import *

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)


async def command_menu(dp: Dispatcher):
  await dp.bot.set_my_commands(
    [
      types.BotCommand('start', 'Ishga tushirish'),
    ]
  )


  await create_tables()

@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
  await add_user(message.from_user.id, message.from_user.username)
  await message.answer("Salom")


@dp.message_handler(content_types=['text'])
async def get_youtube_link_handler(message: types.Message):
  video_url = message.text

  if video_url.startswith("https://youtube") or video_url.startswith("https://youtu.be"):
    video = await download_video(video_url, message.from_user.id)

    wait_msg = await message.answer("⏳")
        
    video = await download_video(video_url, message.from_user.id)
        
    await wait_msg.delete()
        
    if video == "50mb":
          await message.answer("Video xajmi 50mb dan yuqori!")

    if video:
      await message.answer_video(video=types.InputFile(video))
    else:
      await message.answer("Xatolik yuz berdi")

  
if __name__ == "__main__":
  executor.start_polling(dp, on_startup=command_menu)
