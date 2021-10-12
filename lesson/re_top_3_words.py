"""top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"])
top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])
top_3_words("  //wont won't won't "), ["won't", "wont"])
top_3_words("  , e   .. "), ["e"])
top_3_words("  ...  "), [])
top_3_words("  '  "), [])
top_3_words("  '''  "), [])
top_3_words(""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.""), ["a", "of", "on"])

Напишите функцию, которая по заданной строке текста (возможно, с пунктуацией и переносами строк) возвращает массив из
трех наиболее часто встречающихся слов в порядке убывания количества вхождений."""
import collections


import re
from collections import Counter


def top_3_words(text):
    # подсчитать аргумент, пропустить через регулярное выражение и пропустить его
    c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    # вернуть «самые распространенные» 3 символа
    return [w for w, _ in c.most_common(3)]


print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""))
