"""
Цель упражнения — функция collect_indexes(). Эта функция должна принимать на вход коллекцию
(некий iterator/iterable) и возвращать словарь (или подобная ему коллекция!), где ключом будет элемент
коллекции, а значением для ключа — список индексов коллекции, по которым встречается этот элемент.

d = collect_indexes("hello")
d["h"]
[0]
d["e"]
[1]
d["l"]
[2, 3]
"""

from collections import defaultdict


def collect_indexes(arg):
    d = defaultdict(list)
    list_arg = list(arg)
    for i, k in enumerate(list_arg):
        d[k].append(i)
    return d



result = collect_indexes([1])
print(result[1])
print(result)
