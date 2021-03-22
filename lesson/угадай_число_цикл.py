def finde_number_while(run):
    num = 23
    run = True

    while run:
        guess = int(input("Введите целое число:  "))

        if guess == num:
            print("Вы угадали число!")
            run = False
        elif guess < num:
            print("Загаданное число больше этого")
        else:
            print("Загаданное число меньше этого")
    else:
        print("Цикл while закончен")

    print("Завершено")

finde_number_while(int)