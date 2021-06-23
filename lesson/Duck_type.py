def total(a=5, *num, **phonebook):
    print(a)
    for item in num:
        print(num)

    for first, second in phonebook.items():
        print(first, second)

print(total(10,1,2,3, Jack=1123, John=2231, Max=1260))