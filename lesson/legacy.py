# legacy(наследие) создание нового класса из уже существующего, который содержит какое-то дополнение и изменение
# новый класс может автомачитески использовать весь код старого класса

# определим класс Car
# дадим определим метод классу Car
# далее определим подкласс класса Car, который называется Yugo
# далее создадим объекты каждого класса
# далее создадим по одному объекту каждого класса и вызовем их методы exlaim
class Car():
    def exclaim(self):
        print("I'm a Car!")


class Yugo(Car):
    pass


give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()