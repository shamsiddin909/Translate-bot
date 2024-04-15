from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#hhhh
async def choose_lang():
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(
        InlineKeyboardButton("Узбекский", callback_data="lang_uz"),
        InlineKeyboardButton("Русский", callback_data="lang_ru"),
        InlineKeyboardButton("Англиский", callback_data="lang_en"),
        InlineKeyboardButton("Норвежский", callback_data="lang_no"),
        InlineKeyboardButton("Турецкий", callback_data="lang_tr"),
        InlineKeyboardButton("Китайский", callback_data="lang_zh-cn"),
        InlineKeyboardButton("Индонейский", callback_data="lang_id"),
    )
    return btn

