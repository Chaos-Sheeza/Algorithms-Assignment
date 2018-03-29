def rep(lnum):
    lrep, luni = [], []
    while len(lnum) != 0:
        x = 0
        var = lnum[0]
        while var in lnum:
            x = x+1
            lnum.remove(var)
        if x == 1:
            luni.append(var)
        else:
            lrep.append(var)
    return "unique = %s" %luni + "\nrepeated = %s" %lrep


arr = [1,1,2,3,3,3,2,1,4,5,6,7,8,9,7,6]
print(rep(arr))
