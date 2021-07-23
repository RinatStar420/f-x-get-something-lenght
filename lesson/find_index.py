"""
src/solution.py
Цель данного упражнения — реализовать функцию find_second_index(). В этом упражнении вам пригодится
функция find_index(), которую вы реализовали в прошлом упражнении. Напоминаю, эта функция возвращает
индекс первого элемента последовательности, равного заданному значению. Функция find_second_index()
же должна возвращать индекс второго подходящего элемента в последовательности.
Если подходящих элементов в последовательности меньше двух или же последовательность пуста, нужно
всё так же возвращать None.
#find_second_index('b', 'bob')
2
#find_second_index('a', 'cat') is None
True

#find_index('t', 'cat')
#2
#find_index(5, [1, 2, 3, 4, 5, 6, 7])
#4
#find_index(42, []) is None
#True
#find_index('!', 'abc') is None
#True
При выполнении воспользуйтесь циклом for и функцией enumerate().
"""


def find_index(value, items):
    for index, item in enumerate(items):
        if item == value:
            return index


def find_second_index(value, items):
    i = iter(items)
    first = find_index(value, i)
    second = find_index(value, i)
    if second is not None:
        return second + first + 1


#
#
print(find_second_index('b', 'bob'))
