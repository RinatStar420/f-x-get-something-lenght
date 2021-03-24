def total(init=5, *num, extra):
    count = init

    for n in num:
        count+=n

    count+=extra
    print(count)

total(10,1,2,3,extra=20) #первым значением выдаст параметр под звездочкой, параметр extra является ключевым с указанием значения