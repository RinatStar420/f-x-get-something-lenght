"""
get_range() должна для заданного положительного числа аргумента n возвращать список чисел от нуля до n,
не включая само число n. Если при вызове было передано отрицательное число или ноль, функция должна возвращать
пустой список.

#>>> get_range(5)
#[0, 1, 2, 3, 4]

"""


def get_range(num):
    result = []
    counter = 0
    if num < 0:
        return []
    while counter < num:
        result.append(counter)
        counter += 1
    return result


print(get_range(-5))
