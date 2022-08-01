from input import ln
from input import fn
from input import p

lst = [f'Last name: {ln}', f'First name: {fn}', f'Phone: {p}']


def write_pb():
    f = open('/home/efreitor2001/Homeworks/Python_Seminars/HomeWork_7/phonebook.txt', 'a')
    for i in lst:
        f.write('\n' + i)
    f.close()
