"""
Утиная типизация

В питоне имеется также реализация полиморфизма - это значит, что одна операция может быть произведена над
разными объектами независимо от их класса.



Мы не меняем способ инициализации классов QuestionQuote и ExclamationQuote, поэтому не перегружали
методы __init__() родительского класса Quote, чтобы сохранить переменные ообъекта person и words.
Поэтомк мы можем получить доступ к атрибутам self.words  в объектах, созданных с помощью QuestionQuote и
ExclamationQuote

"""
# Используем инициатор  __init__() для всех трёх классов Quote, но добавим две новые функции:
# -who() возвращает значение сохраненной строки person;
# -says() возвращает сохраненную строку words, имеющую особую пунктуацию.
#создадим класс QuestionQuote возвращающий атрибут words с вопросительным значением
#создадим класс ExclamationQuote возвращающий атрибут words с восклицательным значением
#создадим несколько объектов
class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'


class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'


class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'

hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
print(hunter.who(), 'says:', hunter.says())
hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc")
print(hunted1.who(), 'says:', hunted1.says())
hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
print(hunted2.who(), 'says:', hunted2.says())