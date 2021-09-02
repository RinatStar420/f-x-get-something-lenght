"""должен начинаться с хэштега (#).
Все слова должны начинаться с заглавной буквы.
Если окончательный результат длиннее 140 символов, он должен вернуть false.
Если ввод или результат - пустая строка, он должен вернуть false."""


def generate_hashtag(s):
    output = '#'
    if not s:
        return False
    if len(s) > 140:
        return False
    for word in s.split():
        output += word.capitalize()
    return output


print(generate_hashtag("Hello there thanks for trying my Kata"))

# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
