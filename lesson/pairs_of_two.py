"""
tests = (
    ("asdfadsf", ['as', 'df', 'ad', 'sf']),
    ("asdfads", ['as', 'df', 'ad', 's_']),
    ("", []),
    ("x", ["x_"]),
"""


def pairs_of_two(s):
    """Эта функция делинт аргумент(строку) на пары символы в случае четного колличества символов
     в случае, если количесво символов нечетное, то для последней создания последней пары добаляется
     символ '_'."""
    j = ''.join(s)
    if len(j) % 2 == 0:
        return [j[i:i + 2] for i in range(0, len(j), 2)]
    else:
        a = j + '_'
        return [a[i:i + 2] for i in range(0, len(j), 2)]


print(pairs_of_two('sdfadsfa'))
