def qt_05(f,ls):
    qtd = 0
    for x in ls:
        if x == f:
            qtd = qtd + 1
    return qtd
print(qt_05("GAGC",["TACG", "GAGC", "ATUC", "TAGC", "GAGC"]))