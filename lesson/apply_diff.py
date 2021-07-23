"""
Цель упражнения — функция apply_diff(). Эта функция принимает два аргумента, первым из которых выступает множество,
которое нужно будет изменять "по месту" (возвращать ничего не нужно). Вторым аргументом функция принимает словарь,
который может содержать ключи 'add' и 'remove' с множествами в качестве значений. Значения по ключу 'add' нужно добавить
в изменяемое множество, а значения по ключу 'remove' — убрать из множества. Прочие ключи в переданном словаре значения
не имеют и обрабатываться не должны.

target = {'a', 'b'}
diff = {'add': {'c'}, 'remove': {'a'}}
apply_diff(target, diff)
target
{'c', 'b'}

Подсказки
Не используйте методы add и discard. В этом упражнении нужно манипулировать множествами "целик

assert apply_diff(set(), {}) is None,
"""


def apply_diff(target, diff):
    if not target:
        return None
    if 'add' in diff.keys():
        func_1 = set(list(diff['add']))
        target.update(func_1)
    if 'remove' in diff.keys():
        func_2 = set(list(diff['remove']))
        target.difference_update(func_2)


print(apply_diff({'a', 'b', 'c'}, {'remove': {'a'}}))
