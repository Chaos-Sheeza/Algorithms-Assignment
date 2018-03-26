def fibi(n):
    l = [0,1,0]
    sm = 0
    for i in range(n):
        l[2] = l[0] + l[1]
        sm = (sm+l[1])
        l[0] = l[1]
        l[1] = l[2]
    return sm

def fibr(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibr(n-1)+fibr(n-2)

def sumfibr(n):
    res = 0
    for i in range(1,n+1):
        res = res + fibr(i)
    return res


print("Recursive = %d\n" % sumfibr(10) + "Iterative = %d" % fibi(10))
