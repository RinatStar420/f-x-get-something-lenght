def definition_long_string(len):
    while  True:
        s = input("Введите текс: ")
        if s == 'exit':
            break
        if len(s)<3:
            print("Слишком мало")
            continue
        if len(s)>3:
            print("Слишком много")
            continue
        print("Введена строка достаточной длинны")

    print("Завершение")

definition_long_string(len)