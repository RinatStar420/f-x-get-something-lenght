def binary_array_to_number(arr):
        return sum(val*(2**idx) for idx, val in enumerate(reversed(arr)))


print(binary_array_to_number([0,0,0,1]))
print(binary_array_to_number([0,0,1,0]))
print(binary_array_to_number([1,1,1,1]))
print(binary_array_to_number([0,1,1,0]))