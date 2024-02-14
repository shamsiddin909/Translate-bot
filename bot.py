import logging

from aiogram import Bot, Dispatcher, executor, types
from utils import translate_user
from bot_keyboard import choose_lang


logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "6830535886:AAH7a-HjiPKt9xBSEymCHbEM09sydUiug5c"

bot = Bot(token=BOT_TOKEN, parse_mode="html")
dp = Dispatcher(bot=bot)


async def set_my_bot_commands(dp: Dispatcher):
   await dp.bot.set_my_commands([
  types.BotCommand("start", "Start bot"),
])


@dp.message_handler(commands=["start"])
async def start_bot(message: types.Message):
  await message.answer("bot")


@dp.message_handler(content_types=["text"])
async def get_user_text(message: types.Message):
  text = message.text
  result = await translate_user(text, "en") 
  btn = await choose_lang()
  await message.answer(result, reply_markup=btn)
  


@dp.callback_query_handler(text_contains="lang")
async def lang_user(call: types.CallbackQuery):
  lang = call.data.split("_")[1]
  text = call.message.text
  result = await translate_user(text, lang)
  if text != result:
    btn = await choose_lang()
    await call.message.edit_text(result, reply_markup=btn)
    



if __name__ == "__main__":
 executor.start_polling(dp, on_startup=set_my_bot_commands,)
