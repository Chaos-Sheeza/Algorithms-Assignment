# Recursive function that find largest number.
def large(lnum):
    # Stopping condition when lnum has only one element.
    if len(lnum) == 1:
        return lnum
    # 3 conditions used. If first element larger than second, remove second, opposite remove first, equal remove
    # whatever, then calls the function again. By the end there should only be one element left, which is the largest.
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