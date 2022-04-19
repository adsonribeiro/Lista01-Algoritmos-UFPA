def qt_02 (media,ls):
    qtd = 0
    for x in ls:
        if x > media:
            qtd = qtd + 1
    return qtd
print(qt_02(6,[6, 6, 5, 8, 6, 5, 4, 6]))