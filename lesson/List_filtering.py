def filter_list(l):
    new_list = []
    for x in l:
        if type(x) == int:
            new_list.append(x)
    return new_list


print(filter_list([1,2,'a','b']))