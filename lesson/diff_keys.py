"""В этом упражнении вам предстоит анализировать изменения, имея старую и новую версии словаря.
Требуется реализовать функцию diff_keys(), которая должна принимать два словаря-аргумента — "старый" и "новый" —
и возвращать словарь с результатами анализа.
Результирующий словарь должен содержать строго три ниже перечисленных ключа:

'kept' — множество ключей, которые присутствовали в старом словаре и остались в новом;
'added' — множество ключей, которые отсутствовали в старом словаре, но появились в новом;
'removed' — множество ключей, которые присутствовали в старом словаре, но в новый не вошли.
diff_keys({'name': 'Bob', 'age': 42}, {})
{'kept': set(), 'added': set(), 'removed': {'name', 'age'}}
diff_keys({}, {'name': 'Bob', 'age': 42})
{'kept': set(), 'added': {'name', 'age'}, 'removed': set()}
diff_keys({'a': 2}, {'a': 1})
{'kept': {'a'}, 'added': set(), 'removed': set()}
Заметьте, значения не сравниваются — только ключи!
"""

"""
def test_diff_keys():
    old = {'x': 100, 'y': 200, 'z': 105}
    new = {'x': 100, 'y': 200, 'velocity': 2.5}
    diff = solution.diff_keys(old, new)
    assert isinstance(diff, dict)
    assert set(diff.keys()) == {'added', 'removed', 'kept'}
    assert diff['kept'] == {'x', 'y'}
    assert diff['added'] == {'velocity'}
    assert diff['removed'] == {'z'}
"""


def diff_keys(old, new):
    return {
        'kept': set(old) & set(new),
        'added': set(new) - set(old),
        'removed': set(old) - set(new)
    }


print(diff_keys({'x': 100, 'y': 200, 'z': 105}, {'x': 100, 'y': 200, 'velocity': 2.5}))
