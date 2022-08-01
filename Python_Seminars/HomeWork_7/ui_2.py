def read_pb_2():
    f = open('/home/efreitor2001/Homeworks/Python_Seminars/HomeWork_7/phonebook.txt')
    print(f.read().replace('\n', ', ').replace(', , ', ';\n'))
    f.close()
