import os


#num = int(input()) # ввод в программу условий данный под num-число
def find_number_in_range(num):
    print(type(num))
    if num < 100:
        print("Меньше 100")
        if num%2==0:
            print("Делится на 2")
        elif num%3==0:
            print("Делится на 3")
    elif num > 100:
        print("Больше 100")
        if num%2==0:
            print("Делится на 2")
        elif num%3==0:
            print("Делится на 3")
    else:
        print("Вы угадали предел")


find_number_in_range(float(input("Введите число: ")))
