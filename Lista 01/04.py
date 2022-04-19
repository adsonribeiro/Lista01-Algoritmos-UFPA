def qt_04 (ls):
    qtd = 0
    soma = 0
    for x in ls:
        if x % 2 == 0:
            soma = soma + x
            qtd = qtd + 1
    media = soma / qtd
    return media
print(qt_04([2, 4, 8, 6]))