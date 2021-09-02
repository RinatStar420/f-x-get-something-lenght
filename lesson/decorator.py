"""
Вам предстоит реализовать декоратор, добавляющий функции мемоизацию. Мемоизация — это запоминание уже вычисленных
результатов, для уже однажды встреченных аргументов.

Для простоты будем считать, что мемоизироваться будут численные функции одного аргумента (аргумент — число,
результат — тоже число).

 from solution import memoized
 @memoized
... def f(x):
...     print('Calculating...')
...     return x * 10
...
 f(1)
Calculating...
10
 f(1)
10
 f(42)
Calculating...
420
 f(42)
420
 f(1)
10
"""


def memoized(function):
    memory = {}

    def inner(argument):
        memoized_result = memory.get(argument)
        if memoized_result is None:
            memoized_result = function(argument)
            memory[argument] = memoized_result

        return memoized_result

    return inner


@memoized
def f(x):
    print('Calculating...')
    return x * 10


print(f(1))
