def get_something_length():
    while True:
        something = input("Enter smth:")
        if something == 'exit':
            break



        if len(something) > 30 and len(something) < 50:
            answer = f"количество символов:{len(something)}"
            print(answer)
            print("Слишком мало")
            continue


        if len(something) > 10 and len(something) < 15:
            print("Слишком мало")


        else:
            print("ты лох")


    print("Завершение")



get_something_length()

