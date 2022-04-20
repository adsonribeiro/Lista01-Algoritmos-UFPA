def qt_02 (ls):
    qtd = 0
    for x in ls:
        if x[0] == "7" or x[0] == "A" :
            qtd = qtd + 1
    return qtd
retirados = qt_02(["78A3B", "BAC44", "CC125R", "AAA77"])
print("A quantidade de sabonetes a serem retirados são:",retirados)