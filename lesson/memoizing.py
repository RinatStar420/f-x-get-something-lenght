""" В этот раз вы снова будете реализовывать мемоизирующий декоратор "memoizing". Но на этот раз декоратор
должен принимать аргумент, задающий максимальное количество запоминаемых значений. При превышении количества
запомненных значений лишние должны быть отброшены, причём сначала — самые старые!

Напоминаю, мемоизируемые функции считать численными функциями одного аргумента. И не забудьте про functools.wraps!

 @memoizing(3)
... def f(x):
...     print('Calculating...')
...     return x * 10
...
 f(1)
Calculating...
10
 f(1)  # будет "вспомнено"
10
 f(2)
Calculating...
20
 f(3)
Calculating...
30
 f(4)  # вытеснит запомненный результат для "1"
Calculating...
40
 f(1)  # будет перевычислено
Calculating...
10"""



from functools import wraps


def memoizing(limit):
    """
    Make decorator
    """

    def wrapper(function):
        """
        Memoize function.
        """
        memory = {}
        order = []

        @wraps(function)
        def inner(argument):
            memoized_result = memory.get(argument)
            if memoized_result is None:
                memoized_result = function(argument)
                memory[argument] = memoized_result
                order.append(argument)
                if len(order) > limit:
                    oldest_argument = order.pop(0)
                    memory.pop(oldest_argument)
            return memoized_result

        return inner

    return wrapper


@memoizing(3)
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(70))


