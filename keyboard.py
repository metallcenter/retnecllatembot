from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton


def generate_register_menu():
    return ReplyKeyboardMarkup([
        [KeyboardButton(text="Зарегистрироваться")],

    ], resize_keyboard=True, one_time_keyboard=True)

def generate_main_menu():
    return ReplyKeyboardMarkup([
        [KeyboardButton(text="Подать заявку"),
        KeyboardButton(text="Профиль")],

    ], resize_keyboard=True, one_time_keyboard=True)

def generate_profile_menu():
    return ReplyKeyboardMarkup([
        [KeyboardButton(text="Изменить профиль"),
        KeyboardButton(text="Вернуться в главное меню")],

    ], resize_keyboard=True, one_time_keyboard=True)

def generate_apply_keyboard():
    return ReplyKeyboardMarkup([
        [KeyboardButton(text="Заявка на ремонт или замену"),
        KeyboardButton(text="Заявка на закуп")],
        [KeyboardButton(text="Вернуться в главное меню")],
    ], resize_keyboard=True, one_time_keyboard=True)

def generate_repair_menu():
    return ReplyKeyboardMarkup([
        [KeyboardButton(text="Ремонт ПК"),
        KeyboardButton(text="Замена клавиатуры")],
        [KeyboardButton(text="Замена мышки"),
        KeyboardButton(text="Ремонт принтера")],
        [KeyboardButton(text="Другое"),
        KeyboardButton(text="Назад")],
    ], resize_keyboard=True, one_time_keyboard=True)

def generate_buy_menu():
    return ReplyKeyboardMarkup([
        [KeyboardButton(text="Покупка ПК"),
        KeyboardButton(text="Покупка клавиатуры")],
        [KeyboardButton(text="Покупка мышки"),
        KeyboardButton(text="Покупка принтера")],
        [KeyboardButton(text="Другое"),
        KeyboardButton(text="Назад")],
    ], resize_keyboard=True, one_time_keyboard=True)


def request_get_contact():
    return ReplyKeyboardMarkup([
        KeyboardButton(text="Отправить контакт", request_contact=True)
    ], resize_keyboard=True)
    


main_menu = InlineKeyboardMarkup(row_width=2)
btnRandom = InlineKeyboardButton(text="Принять заявку", callback_data="btnRandom")

main_menu.insert(btnRandom)
