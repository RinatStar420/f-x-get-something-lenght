def printmax(a, b):
    if a > b:
        print(a, "больше")
    elif a == b:
        print(a, "равно", b)            # созданная функция
    else:
        print(b, "больше")

printmax(3, 4)


x = 5                          # переменная для функции
y = 7

printmax(x, y)