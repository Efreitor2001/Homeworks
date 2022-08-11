from telebot import *

bot = telebot.TeleBot('TOKEN')


def check_wins(b):
    if (b[0] == 'X ' and b[1] == 'X ' and b[2] == 'X \n' or b[0] == '0 ' and b[1] == '0 ' and b[2] == '0 \n' or
            b[3] == 'X ' and b[4] == 'X ' and b[5] == 'X \n' or b[3] == '0 ' and b[4] == '0 ' and b[5] == '0 \n' or
            b[6] == 'X ' and b[7] == 'X ' and b[8] == 'X \n' or b[6] == '0 ' and b[7] == '0 ' and b[8] == '0 \n' or
            b[0] == 'X ' and b[3] == 'X ' and b[6] == 'X ' or b[0] == '0 ' and b[3] == '0 ' and b[6] == '0 ' or
            b[1] == 'X ' and b[4] == 'X ' and b[7] == 'X ' or b[1] == '0 ' and b[4] == '0 ' and b[7] == '0 ' or
            b[2] == 'X \n' and b[5] == 'X \n' and b[8] == 'X \n' or b[2] == '0 \n' and b[5] == '0 \n' and b[
                8] == '0 \n' or
            b[0] == 'X ' and b[4] == 'X ' and b[8] == 'X \n' or b[0] == '0 ' and b[4] == '0 ' and b[8] == '0 \n' or
            b[2] == 'X \n' and b[4] == 'X ' and b[6] == 'X ' or b[2] == '0 \n' and b[4] == '0 ' and b[6] == '0 '):
        return True
    else:
        return False


def pp(lst, message):
    p1 = ''.join(lst)
    mes = p1
    print(mes)
    bot.send_message(message.chat.id, mes)


p = ['1 ', ' 2 ', ' 3\n',
     '4 ', ' 5 ', ' 6\n',
     '7 ', ' 8 ', ' 9\n']
i = 0


@bot.message_handler(content_types=['text'])
def xo(message):
    global i
    global p
    if message.text == '/start':
        p = ['1 ', ' 2 ', ' 3\n',
             '4 ', ' 5 ', ' 6\n',
             '7 ', ' 8 ', ' 9\n']
        i = 0
        bot.send_message(message.chat.id, 'Start game\nХодят X')
        pp(p, message)
    elif message.text.isdigit():
        if i % 2 == 0:
            step = 'X'
            step1 = '0'
        else:
            step = '0'
            step1 = 'X'
        if check_wins(p) is False:
            li = i
            j = message.text
            print(j)
            if (int(j)) % 3 == 0:
                if p[int(j) - 1] != 'X ' and p[int(j) - 1] != 'X \n' and p[int(j) - 1] != '0 ' and p[int(j) - 1] != \
                        '0 \n':
                    p[int(j) - 1] = f'{step} \n'
                    i += 1
                else:
                    bot.send_message(message.chat.id, 'Занято, попробуй ещё раз!')

            else:
                if p[int(j) - 1] != 'X ' and p[int(j) - 1] != 'X \n' and p[int(j) - 1] != '0 ' and p[int(j) - 1] != \
                        '0 \n':
                    p[int(j) - 1] = f'{step} '
                    i += 1
                else:
                    bot.send_message(message.chat.id, 'Занято, попробуй ещё раз!')
            if li != i:
                bot.send_message(message.chat.id, f'Ходят {step1}')
            else:
                bot.send_message(message.chat.id, f'Ходят {step}')
            pp(p, message)
            if check_wins(p) is True:
                bot.send_message(message.chat.id, f'Wins {step}\nEnd game!')
                p = ['1 ', ' 2 ', ' 3\n',
                     '4 ', ' 5 ', ' 6\n',
                     '7 ', ' 8 ', ' 9\n']
                i = 0
            if i > 8:
                j = message.text
                p[int(j) - 1] = f'{step} '
                bot.send_message(message.chat.id, 'Friendship won\nEnd game!')
                p = ['1 ', ' 2 ', ' 3\n',
                     '4 ', ' 5 ', ' 6\n',
                     '7 ', ' 8 ', ' 9\n']
                i = 0


print('run')
bot.polling(non_stop=True)
