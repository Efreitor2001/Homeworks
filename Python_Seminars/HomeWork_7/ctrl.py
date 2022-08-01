from commands import cmd


def start():
    cmd.lower()
    if cmd == 'add':
        from pb_writer import write_pb
        write_pb()
    elif cmd == 'list':
        ui = int(input('Select display option (1 or 2): '))
        if ui == 1:
            from ui_1 import read_pb_1
            read_pb_1()
        elif ui == 2:
            from ui_2 import read_pb_2
            read_pb_2()
        else:
            print('Error select display option')
    else:
        print('Error command')
