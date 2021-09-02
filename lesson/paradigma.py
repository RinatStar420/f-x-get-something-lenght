""" Вам предстоит реализовать два решения одной и той же задачи — функциональное и процедурное.
Задача состоит в том, чтобы для входного списка списков получить список нечётных по порядку списков
(первый, третий и так далее), оставив в каждом только нечётные по порядку элементы. Например,
для из списка [[1, 2, 3], [4, 5, 6], [7, 8, 9]] должен получиться список [[1, 3], [7, 9]].

При этом функциональное решение должно вычислять новый список списков на основе оригинального.
Оригинальный же список должен оставаться неизменным. У вас должна получиться функция odds_from_odds():

>> from solution import odds_from_odds
>> l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>> odds_from_odds(l)
[[1, 3], [7, 9]]
>> l  # оригинал не изменился!
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>> odds_from_odds([])  # пустой список не должен быть проблемой
[]
>> odds_from_odds([[]])  # как и список пустых списков
[[]]
>>

Процедурное решение должно изменить список-аргумент по месту, а не возвращать его новую версию
(возвращать вообще ничего не нужно!). Постарайтесь обойтись без создания вспомогательных структур в том числе
и для обработки вложенных списков: процедурное решение должно быть эффективным с точки зрения использования памяти,
ведь для этого мы такой код и пишем! У вас должна получиться процедура keep_odds_from_odds():

>> from solution import keep_odds_from_odds
>> l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>> keep_odds_from_odds(l)  # процедура ничего не возвращает
>> l  # но меняет аргумент
[[1, 3], [7, 9]]
>> keep_odds_from_odds(l)
>> l
[[1]]
>> keep_odds_from_odds(l)
>> l  # тут уже ничего чётного не осталось, поэтому никаких изменений нет
[[1]]
>> keep_odds_from_odds([])  # пустой список не должен быть проблемой
>> keep_odds_from_odds([[]])  # как и список пустых списков"""

# BEGIN
from operator import itemgetter

odds = itemgetter(slice(None, None, 2))
# ^ функция, которая вычисляет срез [::2] от аргумента


def odds_from_odds(list_of_lists):
    return list(map(odds, odds(list_of_lists)))


def keep_odd(some_list):
    print(some_list)
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

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("debug: ", odds_from_odds(a))
print(keep_odds_from_odds(a))