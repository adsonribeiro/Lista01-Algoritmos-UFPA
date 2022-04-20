def qt_01 (ls):
    dec = 0
    c = 0
    for x in ls:
        c = c + 1
        if x == 1:
            dec = dec + (c*(x**2))
    return dec
decimal = qt_01([0,0,0,1,1,0,1])
print("O binário em decimal é:",decimal)