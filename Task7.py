def large(lnum):
    if len(lnum) == 1:
        return lnum
    else:
        if lnum[0] > lnum[1]:
            lnum.remove(lnum[1])
            large(lnum)
            return lnum
        elif lnum[0] < lnum[1]:
            lnum.remove(lnum[0])
            large(lnum)
            return lnum
        elif lnum[0] == lnum[1]:
            lnum.remove(lnum[1])
            large(lnum)
            return lnum


print(large([1,2,3,40,5,5,4,6,7,8,9,110]))