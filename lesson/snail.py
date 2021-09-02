def snail(array):
    a = []
    while array:
        a.extend(list(array.pop(0)))
        array = list(zip(*array))
        array.reverse()
    return a



mat = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
# [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(snail(mat))


"""
a.extend(list(array.pop(0)))  - добавляет содержимое seq в список.
a = [1, 2, 3]
array = [[4, 5, 6], [7, 8, 9]]
array = list(zip(*array))
array = [(4, 7), (5, 8), (6, 9)]
array.reverse()
array = [(6, 9), (5, 8), (4, 7)]
a.extend(list(array.pop(0)))
a = [1, 2, 3, 6, 9]
array = [(5, 8), (4, 7)]
array = list(zip(*array))
array = [(5, 4), (8, 7)]
array.reverse()
array = [(8, 7), (5, 4)]
"""


