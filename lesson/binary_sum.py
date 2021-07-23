"""
Реализуйте функцию binary_sum, которая принимает на вход два двоичных числа (в виде строк) и возвращает их сумму.
Результат (вычисленная сумма) также должен быть бинарным числом в виде строки.

Посмотрите примеры работы функции:

binary_sum('10', '1')      # 11
binary_sum('1101', '101')  # 10010
"""

def binary_sum(arg1, arg2):
    first_num = int(arg1, 2)
    second_num = int(arg2, 2)
    summary = first_num + second_num
    result = bin(summary)
    return result[2:]

print(binary_sum('10', '1'))