# в legacy класс можно добавить метов, которого не было в родительском классе
# определим класс и подкласс Car and Yugo
# определим метод need_a_push() только для подкласса Yugo
# далее создадим объекты классов Car and Yugo
# объект класса Yugo может реагировать на метод need_a_push()
class Car():
    def __init__(self):
        print("I'm a Car!")


class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! much like a Car, but more Yugo-ish.")

    def need_a_push(self):
        print("A little help here?")


give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_yugo.need_a_push()
