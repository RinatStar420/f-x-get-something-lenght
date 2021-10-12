import copy
import itertools


def my_map(func, arg):
    yield map(func, arg)


a = my_map(abs, [-1, -2, -3])

for n in a:
    print(list(n))


def my_filter(func, arg):
    yield filter(func, arg)

b = my_filter(lambda x: x % 2 == 1, range(10))

for n in b:
    print(list(n))

from itertools import  chain

def replicate_each(call, arg):
    num = []
    symbol = []
    char = list(chain(arg * call))
    for i in char:
        if type(i) == int:
            num.append(i)
        else:
            symbol.append(i)
    yield (num + symbol)



c = replicate_each(0, [1, 2, 3])
for n in c:
    print(list(n))






#
#
#
#
# print(replicate_each(3, [1, 'a']))
#
# for n in c:
#     print(n)
