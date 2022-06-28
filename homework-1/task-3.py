"""
Задача №3.
Написать метод zeros, который принимает на вход целое число (integer) и
возвращает количество конечных нулей в факториале (N! = 1 * 2 * 3 * ... * N) заданного числа:

Будьте осторожны 1000! имеет 2568 цифр.

Доп. инфо: http://mathworld.wolfram.com/Factorial.html
"""


def zeros(n):
    count = 0
    i = 5
    while i < n:
        count = count + n // i
        i = i * 5
    return count
