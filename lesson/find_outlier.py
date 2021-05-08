def find_outlier(integers):
    even = []
    odd = []
    for i in integers:
        if i % 2 > 0:
            odd.append(i)
        if i % 2 == 0:
            even.append(i)
    if len(odd) < len(even):
        return odd[0]
    else:
        return even[0]



print(find_outlier([2, 4, 6, 8, 10, 3]))
print(find_outlier([160, 3, 1719, 19, 11, 13]))