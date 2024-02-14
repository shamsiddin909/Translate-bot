from googletrans import Translator

tran = Translator()

async def translate_user(text, to_lang):   
    text = tran.translate(text=text, dest=to_lang)
    return text.text

