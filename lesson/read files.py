# создать файл с расширением txt
# наполнить файл содержимым: Фамилия имя отчество 78912345
def create_contacts_file(arg1): # (def)объявление функции, но не вызов

    contacts = open('контакты.txt', 'a') # (a - append добавление текста без перезаписи) это страка открытый файл
    for item in range(0,3): #item - абстрактная строка
        print(item)
        print(arg1[item])
          #надо табать для изменения области видимости для открытой функции
        arg1[item] = arg1[item] + '\n'
        contacts.write(arg1[item]) # запуск записи файла


def read_file(path_to_file):
    file = open(path_to_file, 'r')
    content = file.read()
    return content


arr_contact = ['Иванов И.И. 1234', 'Петров П.П. 2345', 'Семенов С.С. 45678'] # массиы с текстом
#create_contacts_file(arr_contact) # вызов функции

print(read_file('cortege.py'))
