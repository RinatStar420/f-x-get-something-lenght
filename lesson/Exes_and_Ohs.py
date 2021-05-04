def xo(s):
    counter_o = 0
    counter_x = 0
    for letter in s:
        if letter == 'o' or letter == 'O':
            counter_o += 1
        if letter == 'x' or letter == 'X':
            counter_x += 1

    if counter_o == counter_x:
        return True
    else:
        return False

print(xo('xo'))
print((xo('xo0')))
print((not xo('xxxoo')))