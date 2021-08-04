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
    c = len(j)
    n = 2
    if c % 2 == 0:
        return [j[i:i + n] for i in range(0, c, n)]
    else:
        a = j + '_'
        return [a[i:i + n] for i in range(0, c, n)]



print(pairs_of_two(''))