def qt_10(ls):
    qtd = []
    for x in ls:
        if x[0] == "R" or x[0] == "r":
            qtd.append(x)
    return qtd
print(qt_10(["Roger", "Ricardo", "Renato", "Raquel", "Rafaela"]))