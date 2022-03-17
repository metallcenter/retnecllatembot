 
 
    # database, cursor = connect_database()
    # chat_id = message.chat.id

    # try:
    #     cursor.execute("UPDATE users SET phone_number == ? WHERE chat_id == ?", (phone_number, message.chat.id))
    # except:
    #     pass
    # else:
    #     database.commit()        
    # finally:
    #     name = cursor.execute("SELECT name from users where chat_id == ?", (chat_id, )).fetchone()[0]
    # await bot.send_message(message.chat.id, f"{name} вы успешно прошли регистрацию")
    # database.close() 
    # await state.finish()
    # await back_to_main_menu(message)


    # try:
    #     cursor.execute("SELECT name, second_name, phone_number from users where chat_id == ?", (chat_id)).fetchall()

# {"id": "1654416770162106258", "from": 
#     {"id": 385198921, "is_bot": false, "first_name": "М", "username": "m2000ka", "language_code": "ru"}, "message": {"message_id": 1235, "from": {"id": 5084637816, "is_bot": true, "first_name": "MC_BOT", "username": "metall_center_bot"}, "chat": {"id": -761682109, "title":
#     "Заявки", "type": "group", "all_members_are_administrators": true}, "date": 1647348965, "text": "Новая заявка от пользователя Камолходжаев Муродходжа на Ремонт клавиатуры или мышки. Номер телефона 998998887920", "reply_markup": {"inline_keyboard": [[{"text": "Принять заявку", "callback_data": "btnRandom"}]]}}, "chat_instance": "-7623920422800044951", "data": "btnRandom"
#     }
# {"id": "1654416771773018898", "from": 
#     {"id": 385198921, "is_bot": false, "first_name": "М", "username": "m2000ka", "language_code": "ru"
#         }, 
# "message": {"message_id": 1248, "from": {"id": 5084637816, "is_bot": true, "first_name": "MC_BOT", "username": "metall_center_bot"}, "chat": {"id": -761682109, "title":
#     "Заявки", "type": "group", "all_members_are_administrators": true}, "date": 1647349214, "text": "Новая заявка от пользователя Камолходжаев Муродходжа на Требуется замена картриджа. Номер телефона 998998887920", "reply_markup": {"inline_keyboard": [[{"text": "Принять заявку", "callback_data": "btnRandom"}]]}}, "chat_instance": "-7623920422800044951", "data": "btnRandom"
#     }




def check_register():
    message = input()
    if message.isalpha():
        print(message)
    else:
        print("Введите заново")
        check_register()

check_register()