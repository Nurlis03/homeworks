"""
Задача №5.
Написать метод count_find_num, который принимает на вход список простых множителей (primesL) и целое число,
предел (limit), после чего попробуйте сгенерировать по порядку все числа.
Меньшие значения предела, которые имеют все и только простые множители простых чисел primesL.

primesL = [2, 5, 7]
limit = 500
List of Numbers Under 500          Prime Factorization
___________________________________________________________
           70                         [2, 5, 7]
          140                         [2, 2, 5, 7]
          280                         [2, 2, 2, 5, 7]
          350                         [2, 5, 5, 7]
          490                         [2, 5, 7, 7]
"""

import math
import itertools

def count_find_num(primesL, limit):
    dict_for_combs = {}
    for p in primesL:
        log_limit = math.floor(math.log(limit, p))
        dict_for_combs[p] = [x for x in range(1, log_limit + 1)]
    combinations = itertools.product(*dict_for_combs.values())
    res_set = set()
    for comb in combinations:
        num = 1
        for i in range(len(primesL)):
            num *= primesL[i] ** comb[i]
        if num <= limit:
            res_set.add(num)
    if res_set:
        return [len(res_set), max(res_set)]
    else:
        return []