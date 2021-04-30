def order(sentence):
    return ' '.join(sorted([i for i in sentence.split()], key=lambda i: [int(n) for n in i if n.isdigit()][0]))






print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r pe6ople g3ood th5e the2"))
print(order(""))