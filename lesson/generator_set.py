"""
Вам необходимо реализовать функцию number_of_unique_letters(), которая должна подсчитывать количество уникальных букв
в строке-аргументе без учёта регистра.

from solution import number_of_unique_letters
number_of_unique_letters("")
0
number_of_unique_letters("abc")
3
number_of_unique_letters("A-a-a-a-a-a!")
1
number_of_unique_letters("\\(O_o)/")
1
number_of_unique_letters("AaBbCcDd")
4
"""
def func(arg):
    return len({x for x in arg.lower() if x.isalpha()})


one = ""
two = "abc"
three = "A-a-a-a-a-a!"
fore = "\\(O_o)/"
five = "AaBbCcDd"
print(func(one))
print(func(two))
print(func(three))
print(func(fore))
print(func(five))





