# Function creates 2 arrays, one for repeated values, the other for unique values. The function copies an element form
# the original array and stores it in a temporary variable, checks and removes all the elements in the array that are
# equal to it, then if the function removed more than 1 elements (using x as a counter), the variable is appended to the
# array of repeated values. Otherwise the variable is appended to the array of unique values.


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
    return "unique = %s" % luni + "\nrepeated = %s" % lrep


arr = [1, 1, 2, 3, 3, 3, 2, 1, 4, 5, 6, 7, 8, 9, 7, 6]
print(rep(arr))
