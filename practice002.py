# -*- coding:UTF-8 -*-
bonus1 = 100000L * 0.1
bonus2 = bonus1 + 100000L * 0.075
bonus4 = bonus2 + 200000L * 0.05
bonus6 = bonus4 + 200000L * 0.03
bonus10 = bonus6 + 400000L * 0.015



while 1:
    i = int(raw_input("Input gain:\n"))
    if i <= 100000L:
        bonus = i * 0.1
    elif i <= 200000L:
        bonus = bonus1 + (i - 100000L) * 0.075
    elif i <= 400000L:
        bonus = bonus2 + (i - 200000L) * 0.05
    elif i <= 600000L:
        bonus = bonus4 + (i - 400000L) * 0.03
    elif i <= 1000000L:
        bonus = bonus6 + (i - 600000L) * 0.015
    else:
        bonus = bonus10 + (i - 1000000l) * 0.01

    print "bonus:",bonus

