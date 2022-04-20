def qt_03(ls):
    maior  = ls[0]
    for x in ls:
        if x > maior:
            m = x
        if x <= maior:
            me = x
    diferenca = m - me
    return diferenca
print(qt_03([100, 80, 70, 120, 50]))