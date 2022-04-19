def qt_03 (r,ls):
    qtd = 0
    soma = 0
    for x in ls:
        soma = soma + x
        if soma <= r:
            qtd = qtd + 1
    return qtd
print(qt_03(20,[2, 3, 4, 7, 1, 2, 30, 13, 25, 1, 3]))