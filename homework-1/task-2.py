"""
Задача №2.
Написать метод int32_to_ip, который принимает на вход 32-битное целое число
(integer) и возвращает строковое представление его в виде IPv4-адреса:

2149583361 -> "128.32.10.1"
32         -> "0.0.0.32"
0          -> "0.0.0.0"
"""


def int32_to_ip(int32):
    b = ''
    i = 1
    while int32 > 0:
        if i != 8:
            b = str(int32 % 2) + b
        else:
            b = "." + str(int32 % 2) + b
            i = 0
        i += 1
        int32 = int32 // 2
    while len(b) < 36:
        b = '0' + b
        if len(b) == 8 or len(b) == 16 or len(b) == 24 or len(b) == 36:
            b = '.' + b

    b = b.split('.')
    b.pop(0)
    for i in range(len(b)):
        b[i] = str(int(b[i], 2))

    return ".".join(b)
