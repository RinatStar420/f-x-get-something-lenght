"""Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
Выведите все элементы, которые меньше 5."""

"""Также можно воспользоваться функцией filter, которая фильтрует элементы согласно заданному условию"""

# print(list(filter(lambda elem: elem < 5, a)))

# def smaller_5(arg):
#     for elem in arg:
#         if elem < 5:
#             print(elem)
#
#
# print(smaller_5([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]))

"""Даны списки:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
Нужно вернуть список, который состоит из элементов, общих для этих двух списков."""

# def search_double(a, b):
#     c = []
#     for i in a:
#         for j in b:
#             if i == j:
#                 c.append(i)
#                 break
#     return c

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# с помощью filter
# result = list(filter(lambda elem: elem in b, a))
# print(result)

# с помощью включения списка
# result = [elem for elem in a if elem in b]


"""Напишите программу для слияния нескольких словарей в один."""
# dict_a = {1:10, 2:20}
# dict_b = {3:30, 4:40}
# dict_c = {5:50, 6:60}
#
# result = {}
# for d in (dict_a, dict_b, dict_c):
#     result.update(d)

"""Отсортируйте словарь по значению в порядке возрастания и убывания."""

import operator

# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
"""Сортируем в порядке возрастания"""

# result = dict(sorted(d.items(), key=operator.itemgetter(1)))
#
# print(result)

"""в порядке убывания"""

# result = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))


"""Найдите три ключа с самыми высокими значениями в словаре"""

# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
#
# result = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
#
# print(result)

"""Напишите код, который переводит целое число в строку, при том что его можно применить в любой системе счисления"""
#
# def return_str(arg):
#     if type(arg) == str:
#         return int(arg, 2)
#     else:
#         return str(arg)
#
# print(return_str('110'))


"""Нужно вывести первые n строк треугольника Паскаля. В этом треугольнике на вершине и по бокам стоят единицы,
 а каждое число внутри равно сумме двух расположенных над ним чисел"""

# def PrintPasTriangle(rows):
#     row = [1]
#     for i in range(rows):
#         print(row)
#         row = [sum(x) for x in zip([0] + row, row + [0])]
#
#
# PrintPasTriangle(10)


# Пояснение: Добавить все элементы в список и распечатать результат в последний раз
# num = 10
# triangle = [1, [1, 1]]
# for i in range(2, num):
#     cur = [1]  # Определить начальное значение нового списка cur --current
#     pre = triangle[i - 1]  # Извлечь все элементы в первом столбце новой строки для использования
#     for j in range(i - 1):  # Определите предел сложения два на два, то есть максимальное значение i-2
#         cur.append(pre[j] + pre[j + 1])  # Итерировать и добавлять последовательно
#     cur.append(1)  # Хвостовая вставка номер 1 более эффективна, чем использование метода вставки. Она добавляется только в хвостовой части. # Вам не нужно перемещать элемент назад при каждой вставке, поэтому, хотя метод вставки можно отключить, он слишком неэффективен и занимает больше памяти.

# triangle.append(cur)  # Вставить вновь созданный список в список
#     cur=[1]
#     for j in range(0,i-1):
#         cur.append(triangle[i-1][j]+triangle[i-1][j+1])
#     cur.append(1)
#     triangle.append(cur)
# print (cur) # (Сравните строку комментария, результаты двух методов совпадают, операция немного изменена, оба являются списками индексов, и независимо от того, печатается ли она в строке или печатается)


# print(triangle)


"""Напишите проверку на то, является ли строка палиндромом. Палиндром — это слово или фраза, 
которые одинаково читаются слева направо и справа налево."""


# def is_polindrom(string):
#     result = ''
#     i = len(string) - 1
#     while i >= 0:
#         result = result + string[i]
#         i -= 1
#     if string == result:
#         return True
#     else:
#         return False
#
#
# print(is_polindrom('loh'))

"""Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды"""

# seconds = 3600000064
#
# m, s = divmod(seconds, 60)
# h, m = divmod(m, 60)
# d, h = divmod(h, 24)
#
# result = f'{d}:{h}:{m}:{s}'
# print(result)


# def list_tuple():
#     values = input('Введите числа через запятую: ')
#     ints_as_strings = values.split(',')
#     print(ints_as_strings)
#     ints = map(int, ints_as_strings)
#     print('map', ints)
#     lst = list(ints)
#     tup = tuple(lst)
#     print('Список:', lst)
#     print('Кортеж:', tup)
#
# a= list_tuple()
# print(a)

"""Напишите программу, которая принимает имя файла и выводит его расширение. Если расширение у файла определить
невозможно, выбросите исключение."""

# def get_extension(file):
#     l = file.split('.')
#     if len(l) < 2:  # filename has no dots
#         raise ValueError('the file has no extension')
#     first, *middle, last = file
#     if not last or not first and not middle:
#         # example filenames: .filename, filename., file.name.
#         raise ValueError('the file has no extension')
#     print(file, 'has extension: ', l[-1])
#
# print(get_extension('text'))

"""При заданном целом числе n посчитайте n + nn + nnn"""

def solve(n):
    return n + int(str(n)*2) + int(str(n)*3)
print(solve(5))

