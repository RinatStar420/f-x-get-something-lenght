"""
Реализуйте функцию find_longest_length(), принимающую на вход строку и возвращающую длину максимальной
последовательности из неповторяющихся символов. Подстрока может состоять из одного символа.
Например в строке qweqrty, можно выделить следующие подстроки: qwe, weqrty. Самой длинной будет weqrty,
а её длина — 6 символов.

 find_longest_length('abcdeef')
5
 find_longest_length('jabjcdel')
7
"""


def find_longest_length(arg):
    checklist = {}
    count = 0
    length = 0
    for i, v in enumerate(arg):
        if v in checklist:
            count = max(count, checklist[v] + 1)
        checklist[v] = i
        length = max(length, i - count + 1)
    return length


print(find_longest_length(''))  # == 0
print(find_longest_length('a'))  # == 1
print(find_longest_length('jabjcdel'))  # == 7
print(find_longest_length('abcddef'))  # == 4
print(find_longest_length('abbccddeffg'))  # == 3
print(find_longest_length('abcd'))  # == 4
print(find_longest_length('1234561qweqwer'))  # == 9
