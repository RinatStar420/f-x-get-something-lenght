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
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(19))


