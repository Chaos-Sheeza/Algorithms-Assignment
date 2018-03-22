def fact(num):
    res = 1
    for i in range(1,num+1):
        res = res*i
    return res


def cos(x):
    res = 0
    for i in range(85):
        num1 = (-1)**i
        num2 = x**(2*i)
        num3 = float(num1*num2)
        num4 = float(fact(i*2))
        num5 = num3/num4
        res = res + num5
    return res