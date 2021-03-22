def definition_long_string(len): # def - объявление функции
    while True:
        s = input("Введите текс: ")  # input - считывает строку (выводит ее в терминал где мы ее заполняем)
        if s == 'exit':
            break
        if len(s)<3: # len -  количество символов (длинна строки)
            print("Слишком мало")
            continue
        if len(s)>3:
            print("Слишком много")
            continue
        print("Введена строка достаточной длинны")

    print("Завершение")

definition_long_string(len) # вызов функции