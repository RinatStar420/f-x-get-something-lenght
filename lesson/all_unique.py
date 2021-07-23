"""
Вам предстоит реализовать функцию all_unique(), которая должна принимать итератор
(в т.ч. и те, которые не перезапускаемые!) и возвращать True, если элементы в итераторе не повторяются
(если элементов нет, то ничего не повторяется!). Пример работы функции:

all_unique([])
True
all_unique("cat")
True
all_unique([1, 2, 3])
True
all_unique([1, 2, 1])
False
"""


def all_unique(arg):
    item = list(arg)
    return len(item) == len(set(item))


print(all_unique([1, 2, 1]))
