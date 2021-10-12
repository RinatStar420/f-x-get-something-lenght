"""
# -*- coding: utf-8 -*-
solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]) ==> "apples, pears\ngrapes\nbananas"
solution("a #b\nc\nd $e f g", ["#", "$"]), ==> "a\nc\nd"
"""

import re


def solution(string, markers):
    # сплитую по переносу строки
    lines = string.split('\n')
    # нумерую полученные элементы списка
    for i, line in enumerate(lines):
        # условия для маркеров
        for marker in markers:
            # поиск индекса маркера
            index = line.find(marker)
            # если индекс маркера не -1, то возвращаем строку до указанного индекса
            if index != -1:
                line = line[:index]
        lines[i] = line.rstrip(' ')

    return '\n'.join(lines)


print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ['#', '!']))
