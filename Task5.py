# a function that finds the closest guess to the root
def guess(num):
    if num > 100:
        #loop that increases the power of 10 each iteration, until number is smaller than 100
        n = num
        i = 0
        while n > 100:
            i += 1
            n = num/(10**i)
        if i % 2 != 0:
            i = i-1
        num1 = num/(10**i)
    elif num < 1:
        n = num
        i = 0
        while n < 1:
            n = num/(10**i)
            i -= 1
        if i % 2 != 0:
            i = i+1
        num1 = num/(10**i)
    else:
        i = 0
        num1 = num
    for x in range(int(num1)):
        y = x**2
        if y == num1:
            return x*(10**(i/2))
        elif y > num1:
            z = (x-1)**2
            if num1-z > y-num1:
                return x*(10**(i/2))
            else:
                return (x-1)*(10**(i/2))


def sqrt(n):
    if n == 2:
        n1 = 1
    elif n == 1:
        return 1
    elif n == 0:
        return 0
    elif n < 0:
        return "square root is imaginary"
    else:
        n1 = guess(n)
    x = n
    for i in range(10):
        y = float(n/n1)
        n1 = float((y+n1)/2)
    return n1