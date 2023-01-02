import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
import requests

# function


def get_surah(surah, oyat=None):
    if oyat:
        response = requests.get(
            f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu/{surah}/{oyat}.json")
        return response.json()
    else:
        response = requests.get(
            f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu/{surah}.json")
        return response.json()


surahs = [
    "Al-Fatihah(the Opening)",
    "Al-Baqarah(the Cow)",
    "Aali Imran(the Family of Imran)",
    "An-Nisa’ (the Women)",
    "Al-Ma’idah(the Table)",
    "Al-An’am(the Cattle)",
    "Al-A’raf(the Heights)",
    "Al-Anfal(the Spoils of War)",
    "At-Taubah(the Repentance)",
    "Yunus(Yunus)",
    "Hud(Hud)",
    "Yusuf(Yusuf)",
    "Ar-Ra’d(the Thunder)",
    "Ibrahim(Ibrahim)",
    "Al-Hijr(the Rocky Tract)",
    "An-Nahl(the Bees)",
    "Al-Isra’ (the Night Journey)",
    "Al-Kahf(the Cave)",
    " Maryam(Maryam)",
    "Ta-Ha(Ta-Ha)",
    "Al-Anbiya’ (the Prophets)",
    "Al-Haj(the Pilgrimage)",
    "Al-Mu’minun(the Believers)",
    "An-Nur(the Light)",
    "Al-Furqan(the Criterion)",
    "Ash-Shu’ara’ (the Poets)",
    "An-Naml(the Ants)",
    "Al-Qasas(the Stories)",
    "Al-Ankabut(the Spider)",
    "Ar-Rum(the Romans)",
    "Luqman(Luqman)",
    "As-Sajdah(the Prostration)",
    "Al-Ahzab(the Combined Forces)",
    "Saba’ (the Sabeans)",
    "Al-Fatir(the Originator)",
    "Ya-Sin(Ya-Sin)",
    "As-Saffah(Those Ranges in Ranks)",
    "Sad(Sad)",
    "Az-Zumar(the Groups)",
    "Ghafar(the Forgiver)",
    "Fusilat(Distinguished)",
    "Ash-Shura(the Consultation)",
    "Az-Zukhruf(the Gold)",
    "Ad-Dukhan(the Smoke)",
    "Al-Jathiyah(the Kneeling)",
    "Al-Ahqaf(the Valley)",
    "Muhammad(Muhammad)",
    "Al-Fat’h(the Victory)",
    "Al-Hujurat(the Dwellings)",
    "Qaf(Qaf)",
    "Adz-Dzariyah(the Scatterers)",
    "At-Tur(the Mount)",
    "An-Najm(the Star)",
    "Al-Qamar(the Moon)",
    "Ar-Rahman(the Most Gracious)",
    "Al-Waqi’ah(the Event)",
    "Al-Hadid(the Iron)",
    "Al-Mujadilah(the Reasoning)",
    "Al-Hashr(the Gathering)",
    "Al-Mumtahanah(the Tested)",
    "As-Saf(the Row)",
    "Al-Jum’ah(Friday)",
    "Al-Munafiqun(the Hypocrites)",
    "At-Taghabun(the Loss & Gain)",
    "At-Talaq(the Divorce)",
    "At-Tahrim(the Prohibition)",
    "Al-Mulk – (the Kingdom)",
    "Al-Qalam(the Pen)",
    "Al-Haqqah(the Inevitable)",
    "Al-Ma’arij(the Elevated Passages)",
    "Nuh(Nuh)",
    "Al-Jinn(the Jinn)",
    "Al-Muzammil(the Wrapped)",
    "Al-Mudaththir(the Cloaked)",
    "Al-Qiyamah(the Resurrection)",
    "Al-Insan(the Human)",
    "Al-Mursalat(Those Sent Forth)",
    "An-Naba’ (the Great News)",
    "An-Nazi’at(Those Who Pull Out)",
    "‘Abasa(He Frowned)",
    "At-Takwir(the Overthrowing)",
    "Al-Infitar(the Cleaving)",
    "Al-Mutaffifin(Those Who Deal in Fraud)",
    "Al-Inshiqaq(the Splitting Asunder)",
    "Al-Buruj(the Stars)",
    "At-Tariq(the Nightcomer)",
    "Al-A’la(the Most High)",
    "Al-Ghashiyah(the Overwhelming)",
    "Al-Fajr(the Dawn)",
    "Al-Balad(the City)",
    "Ash-Shams(the Sun)",
    "Al-Layl(the Night)",
    "Adh-Dhuha(the Forenoon)",
    "Al-Inshirah(the Opening Forth)",
    "At-Tin(the Fig)",
    " Al -‘Alaq(the Clot)",
    "Al-Qadar(the Night of Decree)",
    "Al-Bayinah(the Proof)",
    "Az-Zalzalah(the Earthquake)",
    "Al -‘Adiyah(the Runners)",
    "Al-Qari’ah(the Striking Hour)",
    "At-Takathur(the Piling Up)",
    "Al -‘Asr(the Time)",
    "Al-Humazah(the Slanderer)",
    "Al-Fil(the Elephant)",
    "Quraish(Quraish)",
    "Al-Ma’un(the Assistance)",
    "Al-Kauthar(the River of Abundance)",
    "Al-Kafirun(the Disbelievers)",
    "An-Nasr(the Help)",
    "Al-Masad(the Palm Fiber)",
    "Al-Ikhlas(the Sincerity)",
    "Al-Falaq(the Daybreak)",
    "An-Nas(Mankind)"
]

buttons = InlineKeyboardMarkup(row_width=3)
full_button = ReplyKeyboardMarkup(resize_keyboard=True)
full_button.insert(KeyboardButton(text="To'liq surani ko'rish !"))
full_button.insert(KeyboardButton(text="Suralarni Ko'rish !"))


for surah in surahs:
    button = InlineKeyboardButton(text=surah, callback_data=surah)
    buttons.insert(button=button)


API_TOKEN = "5805516361:AAGTZWkcYYomgx5wpBJ6jD3O1WKp9EipWfM"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

surah_oyat_state_arr = [0, 1]


@ dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Salom bu bot sizga quranning uzbekcha tarjimasini sizga hovola etadi", reply_markup=buttons)


@ dp.callback_query_handler()
async def send_surah(call: types.CallbackQuery):
    surah_index = surahs.index(call.data)
    surah_oyat_state_arr[0] = surah_index
    await call.message.answer("Iltimos oyat raqamini yuboring\nYoki to'liq surani ko'rish tugmasini bosing !", reply_markup=full_button)


@ dp.message_handler(text="To'liq surani ko'rish !")
async def send(message: types.Message):
    response = get_surah(surah_oyat_state_arr[0] + 1)
    for res in response["chapter"]:
        await message.answer(res["text"])


@ dp.message_handler()
async def send_oyat(message: types.Message):
    surah_oyat_state_arr[1] = message.text
    if surah_oyat_state_arr[0]:
        res = get_surah(surah_oyat_state_arr[0], surah_oyat_state_arr[1])
        await message.answer(res["text"])


@ dp.message_handler(text="Suralarni Ko'rish !")
async def send_menu(message: types.Message):
    await message.answer("Menu", surahs)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
