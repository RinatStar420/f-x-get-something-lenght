"""src/solution.py
Цель упражнения — функция count_all(). Эта функция должна принимать на вход iterable источник и возвращать
словарь, ключами которого являются элементы источника, а значения отражают количество повторов элемента
в коллекции-источнике. Вот пара примеров, демонстрирующих то, как функция должна работать:

 count_all(["cat", "dog", "cat"])
{"cat": 2, "dog": 1}
 count_all("hello")
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
 count_all("*" * 20)
{'*': 20}
"""


# from collections import Counter
#
#
# def count_all(arg):
#     if len(arg) == 1:
#         format_list = ''.join(arg)
#         word_dict_1 = Counter(list(format_list))
#         return word_dict_1
#     else:
#         word_dict_2 = Counter(arg)
#         return word_dict_2

def count_all(arg):
    word_dict = {}
    if len(arg) == 1:
        word_list = list(''.join(arg))
        for k in word_list:
            if k in word_dict:
                word_dict[k] += 1
            else:
                word_dict[k] = 1

        return word_dict
    else:
        for k in arg:
            if k in word_dict:
                word_dict[k] += 1
            else:
                word_dict[k] = 1
        return word_dict


print(count_all(["cat", "dog", "cat"]))
print(count_all(["hello"]))
print(count_all(["*" * 20]))
