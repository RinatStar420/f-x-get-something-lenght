def narcissistic(value):
    # result = []
    # for i in str(value):
    #     result.append(int(i) ** len(str(value)))
    # return sum(result) == value

    return bool(value == sum(int(i) ** len(str(value)) for i in str(value)))










print(narcissistic(7))