"""
функцию make_user(), которая должна принимать два параметра — имя пользователя и возраст (число).
Вернуть функция должна словарь с ключами 'name' и 'age', по которым должны быть сохранены соответствующие
значения.
функцию format_user(), которая, будучи применена к результату вызова make_user() (помним — это словарь),
должна вернуть строку вида 'Phil, 25'.
phil = make_user('Phil', 25)
type(phil)
<class 'dict'>
format_user(phil)
'Phil, 25'
"""


def make_user(name, age):
    return {'name': name, 'age': age}


rinat = make_user('rinat', 25)


def format_user(user):
    return '{}, {}'.format(user["us_name"], user["us_age"])


print(format_user(rinat))
