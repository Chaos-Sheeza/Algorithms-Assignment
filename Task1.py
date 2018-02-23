def pairs(liz):
    for a in range(len(liz)):
        w = liz[a]
        for b in range(len(liz)):
            if liz[b] != w:
                x = liz[b]
                for c in range(len(liz)):
                    if liz[c] != w and liz[c] != x:
                        y = liz[c]
                        for d in range(len(liz)):
                            if liz[d] != w and liz[d] != x and liz[d] != y:
                                z = liz[d]
                                if (w*x) == (y*z):
                                    print("\n(%d,%d),(%d,%d) = %d" % (w, x, y, z, (w*x)))


varx = list(range(1, 1025))
pairs(varx)
