from commands import cmd
from PB_writer import write_pb
from ui_1 import read_pb_1
from ui_2 import read_pb_2


def start():
    cmd.lower()
    if cmd == 'add':
        write_pb()
    elif cmd == 'list':
        ui = int(input('Select display option (1 or 2): '))
        if ui == 1:
            read_pb_1()
        elif ui == 2:
            read_pb_2()
        else:
            print('Error select display option')
    else:
        print('Error command')
