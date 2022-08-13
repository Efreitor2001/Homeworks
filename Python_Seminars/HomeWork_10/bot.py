# 1. Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.(дополнительно)
# (импорт и экспорт)
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import sqlite3

bot = Bot('5443768158:AAEnvpOikdGWfl0H-D96FcZCFkTKQ30xpz0')
dp = Dispatcher(bot)

conn = sqlite3.connect('db/phonebook.db', check_same_thread=False)
cursor = conn.cursor()
print("Подключен к SQLite")


def write_db(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT INTO users (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)',
                   (user_id, user_name, user_surname, username))
    conn.commit()


def add(users_id: int, name_pb: str, name: str, surname: str, about: str, phone: int):
    cursor.execute('INSERT INTO pb (users_id, name_pb, name, surname, about, phone) VALUES(?, ?, ?, ?, ?, ?)',
                   (users_id, name_pb, name, surname, about, phone))
    conn.commit()


def print_pb(message):
    if len(message.text.split()) < 2:
        pb = f"SELECT name_pb FROM pb WHERE users_id = {message.from_user.id}"
        cursor.execute(pb)
        pbs = cursor.fetchall()
        conn.commit()
        res = ''
        mess = str(pbs).replace('[(', '').replace(',), ', ',').replace(',)]', '').replace('(', '') \
            .replace("'", "").split(',')
        for i in mess:
            if i not in res:
                res += i + '\n'
        return res


def print_in_pb(message):
    if len(message.text.split()) == 2:
        pn = "".join(message.text.split()[1])
        pb = f"SELECT name,surname,phone,about FROM pb WHERE users_id = {message.from_user.id} AND name_pb = '{pn}'"
        cursor.execute(pb)
        pbs = cursor.fetchall()
        conn.commit()
        res = str(pbs).replace("[('", '').replace("', '", " ").replace("', ", "\n").replace(", '", "\n") \
            .replace("'), ('", "\n\n").replace("')]", "")
        return res
    else:
        if "".join(message.text.split()[2]) == '1':
            pn = "".join(message.text.split()[1])
            pb = f"SELECT name,surname,phone,about FROM pb WHERE users_id = {message.from_user.id} AND name_pb = '{pn}'"
            cursor.execute(pb)
            pbs = cursor.fetchall()
            conn.commit()
            res = str(pbs).replace("[('", '').replace("', '", " ").replace("', ", ", ").replace(", '", ", ") \
                .replace("'), ('", ";\n").replace("')]", ".")
            return res
        else:
            pn = "".join(message.text.split()[1])
            pb = f"SELECT name,surname,phone,about FROM pb WHERE users_id = {message.from_user.id} AND name_pb = '{pn}'"
            cursor.execute(pb)
            pbs = cursor.fetchall()
            conn.commit()
            res = str(pbs).replace("[('", '').replace("', '", " ").replace("', ", "\n").replace(", '", "\n") \
                .replace("'), ('", "\n\n").replace("')]", "")
            return res


@dp.message_handler(commands=['start'])
async def start(message):
    us_id = message.from_user.id
    us_name = message.from_user.first_name
    us_sname = message.from_user.last_name
    username = message.from_user.username
    await bot.send_message(message.chat.id,
                           '*Добро пожаловать в PbB*\n'
                           '---------------------------------------------------------------------------'
                           '\nВведите команду или /help, чтобы начать работу',
                           parse_mode='markdown')
    write_db(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)


@dp.message_handler(commands=['help'])
async def helps(message):
    await message.reply('/list - Список Ваших книг\n'
                        '<b>Используйте <code>/list - вывести Ваши книги</code>\n'
                        '<code>/list имя_книги способ_вывода(1/2) - вывести контакты из выбранной книги</code></b>\n'
                        '\n/add - Сделать новую запись в телефонную книгу\n'
                        '<b>Используйте <code>/add имя_телефонной_книги* Имя* '
                        'Фамилия Номер* Описание(можно с пробелами)</code>...\n'
                        '"*" - обязательно к заполнению</b>\n\n', parse_mode='html')


@dp.message_handler(commands=['add'])
async def add_pb(message):
    if len(message.text.split()) > 2 and len(message.text.split()) > 4:
        p_name = "".join(message.text.split()[1])
        test = f'SELECT phone FROM pb WHERE users_id == {message.from_user.id}'
        cursor.execute(test)
        check = cursor.fetchall()
        conn.commit()
        u_name = "".join(message.text.split()[2])
        u_surname = "".join(message.text.split()[3])
        u_about = " ".join(message.text.split()[5:])
        u_phone = int("".join(message.text.split()[4]))
        if str(u_phone) in str(check):
            await message.reply('У Вас уже есть такой контакт!!!')
        else:
            u_id = message.from_user.id
            if p_name == ' ':
                await message.reply('<b>Используйте <code>/add имя_телефонной_книги* Имя* '
                                    'Фамилия Номер* Описание(можно с пробелами)</code>...\n'
                                    '* - обязательно к заполнению</b>',
                                    parse_mode='html')
            else:
                add(users_id=u_id, name_pb=p_name, name=u_name, surname=u_surname, about=u_about, phone=u_phone)
                await message.reply('Запись успешно добавлена!')
    elif len(message.text.split()) < 5:
        await message.reply('<b>Телефон не может быть пустым!!!\n'
                            'Используйте <code>/add имя_телефонной_книги* Имя* '
                            'Фамилия Номер* Описание(можно с пробелами)</code>...\n'
                            '"*" - обязательно к заполнению</b>',
                            parse_mode='html')
    else:
        await message.reply('<b>Название книги не может быть пустым!!!\n'
                            'Используйте <code>/add имя_телефонной_книги* Имя* '
                            'Фамилия Номер* Описание(можно с пробелами)</code>...\n'
                            '"*" - обязательно к заполнению</b>',
                            parse_mode='html')


@dp.message_handler(commands=['list'])
async def ppb(message):
    if len(message.text.split()) < 2:
        await message.reply(print_pb(message))
    else:
        await message.reply(print_in_pb(message))


print('run')
executor.start_polling(dp)
