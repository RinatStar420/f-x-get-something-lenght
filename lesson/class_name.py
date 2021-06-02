#добавим параметр name  в метод инициализации
#Создадим объект класса Person, передав строку для параметра name
class Person():
    def __init__(self, name):
        self.name = name
hunter = Person('Elmer Fudd')

print('The mighty hunter: ', hunter.name)