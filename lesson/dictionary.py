#d = {"key1" : 1, "key2"  : 2}# словарь это аналог "адресной книги"
#print(d)

ab = {'Swaroop' : "swaroop@swaroopch.com", # ab созданный словарь
      'Larry': "larry@wall.com",   # ключ и значение разделяются двоеточиями, и все это берется в фигурные скобки
      'Matsumo': "matz@ruby.com",
      'Spammer': "spamer@hot.com"}
print("Адрес Swaroop'a", ab["Swaroop"]) # ab[] использование ключа из списка

del ab["Spammer"]
print("\n В адресной книге: {0} контакта\n".format(len(ab)))
for name, adress in ab.items(): # обращаемся ко всем параметрам ключа ad[] через items
    print("Контакт {0} с адресом {1}".format(name, adress)) # указываем обращение к нашему кортежу
ab["Guido"] = 'guido@python.com' # добавление новой пары ключ/значение 

if "Guido" in ab:
    print("\nАдрес Guido", ab['Guido'])