

def to_jaden_case(string):
    result = string.split()
    print(result)
    output = ''
    i = 0
    while i <= len(result) - 1:
        output += result[i].capitalize()
        i += 1
        # if i == len(result) - 1:
        #     output += result[i].capitalize()
        #     i += 1

    return '#' + output

print(to_jaden_case("how can mirrors                  be real if our eyes           aren't          real"))