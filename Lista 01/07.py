def qt_07(ls):
    qtd = 0
    c = 0
    for x in ls:
        c = c + 1
        if x == c:
            qtd = qtd + 1
    return qtd
print(qt_07([1, 2, 4, 8, 6, 3, 7]))