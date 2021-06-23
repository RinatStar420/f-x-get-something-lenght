"""
Определим новый класс, который называется EmailPerson и представляет объект класса Person, содержащий
адреса электронной почты
"""
#Обратить внимание в легаси появился параметр емаил
#Опледеляя метод __init__() для легаси, заменяется __init__() родительского класса, в результате нужно вызывать его явно
# Метод super() получает определение родительского класса
# __init__() вызывает метод Person.__init__()
# Строка self.email = email - это новый код, который отличает наследие от родителя
# создадим одну персонум
# теперь мы можем обратиться к name и email
class Person():
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

bob = EmailPerson('Bob Frapples', 'bob@frapples.com')

print(bob.name)
print(bob.email)