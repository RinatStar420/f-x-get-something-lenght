"""
В этом упражнении вам нужно будет, используя функцию rgb(), реализовать функцию get_colors(), которая должна вернуть
словарь цветов. В словаре должны присутствовать ключи 'red', 'green','blue'.
Каждому ключу должен соответствовать результат вызова функции rgb() со значением 255 для соответствующего ключу
аргумента. Для построения каждого цвета используйте только один аргумент!

 colors = get_colors()
 set(colors.keys()) == {'red', 'green', 'blue'}
True
 colors['red']
'rgb(255, 0, 0)'
 colors['blue']
'rgb(0, 0, 255)'
"""


def rgb(red=0, green=0, blue=0):
    return 'rgb({}, {}, {})'.format(red, green, blue)


def get_colors():
    return {'red': rgb(red=255),
            'green': rgb(green=255),
            'blue': rgb(blue=255)}


print(set(get_colors()))

color = get_colors()
print(set(color.keys()) == {'red', 'green', 'blue'})
print(color['red'])
