from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery
from keyboard import main_menu, request_get_contact, generate_apply_keyboard, generate_buy_menu, generate_main_menu, generate_profile_menu, generate_register_menu, generate_repair_menu

import os
from dotenv import load_dotenv

from database import connect_database
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

channel_id = "-1001673285930"
group_id = "-761682109"

class FSMhandler(StatesGroup):
    describtion = State()

class FSMAdmin(StatesGroup):
    name = State()
    second_name = State()
    phone_number = State() 

load_dotenv()

token = os.getenv("BOT_TOKEN")
bot = Bot(token)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=["start", "help"])
async def start(message: Message):
    chat_id = message.chat.id
    if message.chat.type != "group":
        full_name = message.from_user.full_name
        await bot.send_message(chat_id, f"Привет {full_name}!")
        await register_user(message)
    else:
        await bot.send_message(chat_id, "Здравствуйте. Скоро начнут поступать заявки!")



async def register_user(message: Message):
    if message.chat.type != "group":
        chat_id = message.chat.id
        full_name = message.from_user.full_name

        database, cursor = connect_database()

        try:
            cursor.execute("""INSERT INTO users (full_name, chat_id)
                VALUES (?, ?)
            """, (full_name, chat_id))
        except:
            await bot.send_message(chat_id, "Главное меню",
                                reply_markup=generate_main_menu())
        else:
            database.commit()
            await show_registrate_menu(message)
        finally:
            database.close()

async def show_registrate_menu(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, "Вам требуется пройти регистрацию",
                           reply_markup=generate_register_menu())


@dp.message_handler(lambda message:"Вернуться в главное меню" in message.text, state=None)
async def back_to_main_menu(message: Message):
    if message.chat.type != "group":
        chat_id = message.chat.id
        await bot.send_message(chat_id, "Главное меню",
                                reply_markup=generate_main_menu())


@dp.message_handler(lambda message:"Зарегистрироваться" in message.text, state=None)
async def cm_start(message: Message):
    await FSMAdmin.name.set()
    await message.reply("Введите ваше имя")


@dp.message_handler(state=FSMAdmin.name)
async def check_register(message: Message, state: FSMContext):
    if message.text.isalpha():
        await load_name(message, state)
    else:
        await bot.send_message(message.chat.id, "Введите имя без знаков и цифр")


async def load_name(message: Message, state: FSMContext):
    name = message.text
    database, cursor = connect_database()
    try:
        cursor.execute("UPDATE users SET name == ? WHERE chat_id == ?", (name, message.chat.id))
    except:
        pass
    else:
        database.commit()
    finally:
        database.close()    

    await FSMAdmin.next()
    await message.reply("Введите вашу фамилию")


@dp.message_handler(state=FSMAdmin.second_name)

async def check_register(message: Message, state: FSMContext):
    if message.text.isalpha():
        await load_second_name(message, state)
    else:
        await bot.send_message(message.chat.id, "Введите имя без знаков и цифр")

async def load_second_name(message: Message, state: FSMContext):
    second_name = message.text
    database, cursor = connect_database()

    try:
        cursor.execute("UPDATE users SET second_name == ? WHERE chat_id == ?", (second_name, message.chat.id))
    except:
        pass
    else:
        database.commit()
    finally:
        database.close() 

    await FSMAdmin.next()
    await message.reply("Отравьте номер для связи:")


@dp.message_handler(state=FSMAdmin.phone_number)

async def check_register(message: Message, state: FSMContext):

    if len(message.text)<=13:
        if len(message.text)>=8:
            await load_phone_number(message, state)
        else:
            await bot.send_message(message.chat.id, "Введенный вами номер телефона не должен быть меньше 9 цифр")
    else:
        await bot.send_message(message.chat.id, "Введенный вами номер телефона не должен превышать 13 цифр")


async def load_phone_number(message: Message, state: FSMContext):    

    phone_number = message.text

    database, cursor = connect_database()
    chat_id = message.chat.id

    try:
        cursor.execute("UPDATE users SET phone_number == ? WHERE chat_id == ?", (phone_number, chat_id))
    except:
        pass
    else:
        database.commit()        
    finally:
        name = cursor.execute("SELECT name from users where chat_id == ?", (chat_id, )).fetchone()[0]
    await bot.send_message(chat_id, f"{name} вы успешно прошли регистрацию")
    database.close() 
    await state.finish()
    await back_to_main_menu(message)


@dp.message_handler(lambda message:"Подать заявку" in message.text, state=None)
async def apply(message: Message):
    if message.chat.type != "group":
        chat_id = message.chat.id
        await bot.send_message(chat_id, message.text,
                            reply_markup=generate_apply_keyboard())


@dp.message_handler(lambda message:"Заявка на ремонт" in message.text, state=None)
async def apply_to_repair(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, message.text,
                        reply_markup=generate_repair_menu())


@dp.message_handler(lambda message:"Заявка на закуп" in message.text, state=None)
async def apply_to_buy(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, message.text,
                        reply_markup=generate_buy_menu())


@dp.message_handler(lambda message:"Назад" in message.text, state=None)
async def go_back(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, message.text,
                        reply_markup=generate_apply_keyboard())


@dp.message_handler(lambda message:"Профиль" in message.text, state=None)
async def open_profile_menu(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, message.text,
                            reply_markup=generate_profile_menu())


@dp.message_handler(lambda message:"Изменить профиль" in message.text, state=None)
async def cm_start(message: Message):
    await FSMAdmin.name.set()
    await message.reply("Введите ваше имя")


@dp.message_handler()
async def take_apply(message: Message):
    if message.text == "Отмена":
        await bot.send_message(message.chat.id, "Отмена", reply_markup=generate_profile_menu())
    if message.text == "Другое":
        await bot.send_message(message.chat.id, "Введите в подробностях вашу заявку")
        await FSMhandler.describtion.set()
    if message.text == "Ремонт ПК" or message.text == "Замена клавиатуры" or message.text == "Замена мышки" or message.text == "Ремонт принтера" or message.text == "Покупка ПК" or message.text == "Покупка клавиатуры" or message.text == "Покупка мышки" or message.text == "Покупка принтера":
        describtion = message.text
        chat_id = message.chat.id
        database, cursor = connect_database()
        user_name = cursor.execute("SELECT name from users where chat_id == ?", (chat_id, )).fetchone()[0]
        user_second_name = cursor.execute("SELECT second_name from users where chat_id == ?", (chat_id, )).fetchone()[0]
        user_phone_number = cursor.execute("SELECT phone_number from users where chat_id == ?", (chat_id, )).fetchone()[0]
        database.close()
        await bot.send_message(channel_id, f"Заявка: {describtion}\nОт: {user_second_name} {user_name}\nНомер телефона:{user_phone_number}",
                                                            reply_markup=main_menu)
        await bot.send_message(message.chat.id, "Ваша заявка была успешно принята ✅\nОжидайте звонка 👨‍💻",
                                                            reply_markup=generate_main_menu())


@dp.callback_query_handler(text="btnRandom")
async def random(message: Message):
    await bot.delete_message(message.message.chat.id, message.message.message_id)
    await bot.send_message(message.message.chat.id, f"{message.message.text}\nЗаявка принято")


@dp.message_handler(state=FSMhandler.describtion)
async def take_describtion(message: Message, state=FSMContext):
    describtion = message.text
    chat_id = message.chat.id
    database, cursor = connect_database()
    user_name = cursor.execute("SELECT name from users where chat_id == ?", (chat_id, )).fetchone()[0]
    user_second_name = cursor.execute("SELECT second_name from users where chat_id == ?", (chat_id, )).fetchone()[0]
    user_phone_number = cursor.execute("SELECT phone_number from users where chat_id == ?", (chat_id, )).fetchone()[0]
    database.close()
    await bot.send_message(channel_id, f"Заявка: {describtion}\nОт: {user_second_name} {user_name}\nНомер телефона:{user_phone_number}",
                                                        reply_markup=main_menu)
    await bot.send_message(chat_id, "Ваша заявка была успешно принято. В скором времени наш персонал свяжется свами",
                                                        reply_markup=generate_main_menu())
    await state.finish()

executor.start_polling(dp, skip_updates=True)



