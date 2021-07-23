
from dadata import Dadata

def get_gender(full_name):
    token = "f1f65baffababb3c9a5f1f89303aa95b671a10a3"
    secret = "0123b896ae0502c432e990444e0dd1a8b4eb8923"
    dadata = Dadata(token, secret)
    result = dadata.clean("name", full_name)
    return result['gender']

def get_smile(gender):
    if gender == 'М':
        return '🧔'
    if gender == 'Ж':
        return '👩'
    else:
        return '👽'

print(get_smile(get_gender('Иванов Иван')))