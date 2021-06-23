#перегузить можно любой метод, включая __init__()
#использую класс Person создадим подклассы, которые представляют доктаров (MDPerson) и адвокатов (JDPerson)
#__init__() принимает те эе методы, что и родительский классБ но внутри сохраняет значение переменной name  разными способами
class Person():
    def __init__(self, name):
        self.name = name

class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name

class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"

person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')

print(person.name)
print(doctor.name)
print(lawyer.name)