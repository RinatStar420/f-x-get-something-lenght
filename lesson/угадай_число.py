
def find_number(num):
    guess = num
    num = 23
    if guess == num:
        print("Вы угадали число!")
    elif guess > num:
        print("Загаданное число меньше этого!")
    else:
        print("Загаданное число больше этого!")


find_number(int(input("Введите целое число: ")))

