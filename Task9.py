# Iterative sum of fibonacci function.
def fibi(n):
    lis = [0, 1, 0]             # Array that stores the two latest values of fibonacci and their addition.
    sm = 0                      # Variable to store the sum.
    # Loop the size of n, adds first and second and stores result in third element of the array, second element added to
    # the sum, since technically the second element is the actual last term, the third is the sum of the last and the
    # term before it.
    for i in range(n):
        lis[2] = lis[0] + lis[1]
        sm = (sm+lis[1])
        lis[0] = lis[1]
        lis[1] = lis[2]
    return sm


# Recursive fibonacci function. Created to compare efficiency.
'''
def fibr(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibr(n-1)+fibr(n-2)


def sumfibr(n):
    res = 0
    for i in range(1, n+1):
        res = res + fibr(i)
    return res
'''

print("Iterative = %d" % fibi(10))
# print("Recursive = %d" % sumfibr(10))
