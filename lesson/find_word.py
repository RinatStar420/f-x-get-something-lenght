import string


def find_missing_letter(chars):
    for letter in string.ascii_uppercase + string.ascii_lowercase:
        if ord(letter) >= ord(chars[0]):
            if letter not in chars:
                return letter


print(find_missing_letter(['a','b','c','d','f'])) #e
print(find_missing_letter(['O', 'Q', 'R', 'S']))  #P
