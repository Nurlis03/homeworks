"""
Задача №4.
Написать метод bananas, который принимает на вход строку и
возвращает количество слов «banana» в строке.

(Используйте - для обозначения зачеркнутой буквы)
Input: bbananana

Output:

b-anana--
b-anan--a
b-ana--na
b-an--ana
b-a--nana
b---anana
-banana--
-banan--a
-bana--na
-ban--ana
-ba--nana
-b--anana
"""

import itertools
def bananas(s) -> set:
    result = set()
    pattern = 'banana'
    enumerated_characters = list(enumerate(s))
    for iteration in itertools.combinations(enumerated_characters, len(pattern)):
        characters_list = list(s)
        if ''.join(j[1] for j in iteration) == pattern:
            for idx, character in enumerate(s):
                if (idx, character) not in iteration:
                    characters_list[idx] = '-'
            result.add(''.join(characters_list))
    return result