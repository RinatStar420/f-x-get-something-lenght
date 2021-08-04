"""
Вам нужно реализовать функцию greet(), которая должна принимать несколько имён (как минимум одно!) и возвращать строку
приветствия (см. примеры ниже).

greet('Bob')
'Hello, Bob!'
greet('Moe', 'Mary')
'Hello, Moe and Mary!'
greet(*'ABC')
'Hello, A and B and C!'
"""


def greet(name, *args):
    arg = ' and '.join(args)
    if name and args:
        return 'Hello, {} and {}!'.format(name, arg)
    else:
        return 'Hello, {}!'.format(name)


print(greet('Mike'))


# b = ' and '.join(list(n))
# print(b)