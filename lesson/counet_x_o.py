def xo(s):
    string = s
    counter_o = 0
    counter_x = 0
    for letter in string:
        if letter == 'o':
            counter_o += 1
        if letter == 'x':
            counter_x += 1

    if counter_o == counter_x:
        return True
    else:
        return False


print(xo('xo'))

print(xo('xo0'))

print(xo('xxxoo'))

