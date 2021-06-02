def divisors(integer):
    dividers = []

    for div in range(2, integer - 1):
        if integer % div == 0:
            dividers.append(div)
    if len(dividers) == 0:
        return f'{str(integer)} is prime'
    else:
        return dividers

print(divisors(24))