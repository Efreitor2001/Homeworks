from input import ln
from input import fn
from input import p
from input import desc

lst = [f'Last name: {ln}', f'First name: {fn}', f'Phone: {p}', f'Description: {desc}']


def write_pb():
    f = open('/home/efreitor2001/Homeworks/Python_Seminars/HomeWork_7/phonebook.txt', 'a')
    for i in lst:
        f.write(i + '\n')
    f.write('\n')
    f.close()
