"""
Вам предстоит реализовать два решения одной и той же задачи — функциональное и процедурное.
Задача состоит в том, чтобы для входного списка списков получить список нечётных по порядку списков
(первый, третий и так далее), оставив в каждом только нечётные по порядку элементы. Например,
для из списка [[1, 2, 3], [4, 5, 6], [7, 8, 9]] должен получиться список [[1, 3], [7, 9]].
При этом функциональное решение должно вычислять новый список списков на основе оригинального. Оригинальный же список
должен оставаться неизменным. У вас должна получиться функция odds_from_odds():
"""

#
#
# def odds_from_odds(num):
#         if num % 2 == 0:
#             return False
#         else:
#             return True
#
# def odds_from_odds_1(func, arg):
#     result = filter(func, arg)
#     return list(result)
#
#
#
# print(odds_from_odds_1( odds_from_odds, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]))



# numbers =

# функция, которая проверяет числа
def filter_odd_num(num):
    for nums in num:
        if nums % 2 == 0:
            return False
        else:
            return True


def filter_odd_num_1(arg):
    out_filter = filter(filter_odd_num, arg)
    c = filter(filter_odd_num, out_filter)
    return list(c)



l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(filter_odd_num_1(l))
print(l)


from operator import itemgetter

odds = itemgetter(slice(None, None, 2))
# ^ функция, которая вычисляет срез [::2] от аргумента


def odds_from_odds(list_of_lists):
    return list(map(odds, odds(list_of_lists)))


def keep_odd(some_list):
    del some_list[1::2]  # noqa: WPS420
    # Инструкция "del", это очень низкоуровневое действие и напрямую
    # использовать его мы не рекомендуем. Но другого способа очистить
    # срез "по месту", да ещё и за одно действие нет,
    # поэтому "del" здесь уместен.
    # Наш линтер за "del" ругает, поэтому пришлось отключить предупреждение!


def keep_odds_from_odds(list_of_lists):
    keep_odd(list_of_lists)  # отбрасываем чётные списки первого уровня
    for one_list in list_of_lists:  # затем в каждом из оставшихся списков...
        keep_odd(one_list)  # ...отбрасываем чётные элементы