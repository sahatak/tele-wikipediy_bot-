import wikipedia
import logging
from aiogram import Bot, Dispatcher# types
from aiogram.types import Message
from aiogram.filters import CommandStart
import asyncio
from googletrans import Translator, LANGUAGES

API_TOKEN = "8265813451:AAEhmk-Jxj5Uo0ckoMNLrIbkxgqBbj9XBbg"
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
translator = Translator()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Salom! Menga istalgan tilda  so‘z yoki mavzu yuboring, men uni tarjima qilib, Wikipedia'dan maqola topaman.")
                         #Hello! Send me a word or topic in any language, I will translate it and find an article on Wikipedia.
@dp.message()
async def wiki_ans(message:Message):
    try:
        k_list = {}
        k = message.text.title()
        # cheklist
        # k = 'この文章は日本語で書かれました。'
        # k = '이 문장은 한글로 쓰여졌습니다.'
        # k = 'Bu gap uzbek tilida yozilgan.'
        # k = 'это предложение написано на русском.'
        # k = 'This sentence is written in English.'
        l1 = await translator.detect(k)
        lang_name = LANGUAGES.get(l1.lang)
        # print(l1.lang)
        if l1.lang == 'en' or l1.lang == 'ru' or l1.lang == 'uz':
            k1 = await translator.translate(k, dest='ru')
            wikipedia.set_lang("ru")
            answeri = wikipedia.summary(k1.text)
            await message.answer(answeri)
            k_list['Russian'] = k1.text
            k2 = await translator.translate(k, dest='en')
            wikipedia.set_lang("en")
            k_list['English'] = k2.text
            answeri = wikipedia.summary(k2.text)
            await message.answer(answeri)
            k_list['English'] = (k2.text)
            k3 = await translator.translate(k, dest='uz')
            wikipedia.set_lang("uz")
            answeri = wikipedia.summary(k3.text)
            await message.answer(answeri)
            k_list['Uzbek'] = k3.text
        for n, m in k_list.items():
            print(f"{n} => {m}")
        else:
            print(f"{lang_name}=> {k}")
            wikipedia.set_lang(l1.lang)
            answeri = wikipedia.summary(message.text)
            await message.answer(answeri)
            k1 = await translator.translate(k, dest='ru')
            wikipedia.set_lang("ru")
            answeri = wikipedia.summary(k1.text)
            await message.answer(answeri)
            k_list['Russian'] = k1.text
            k2 = await translator.translate(k, dest='en')
            wikipedia.set_lang("en")
            k_list['English'] = k2.text
            answeri = wikipedia.summary(k2.text)
            await message.answer(answeri)
            k_list['English'] = k2.text
            k3 = await translator.translate(k, dest='uz')
            wikipedia.set_lang("uz")
            answeri = wikipedia.summary(k3.text)
            await message.answer(answeri)
            k_list['Uzbek'] = k3.text
        for n, m in k_list.items():
            repr(f"{n} => {m}")
    except:
        await message.answer('Bunday maqola umuman topilmadi ')
                            # No such article was found at all.
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
       asyncio.run(main())
