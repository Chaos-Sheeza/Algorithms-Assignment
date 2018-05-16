# Method that finds the factorial of a number.
# Simple method, just multiplies every number before num by using a loop the size of num, and returns the result.


def fact(num):
    res = 1
    for i in range(1, num+1):
        res = res*i
    return res


# Method that solves cosine using Maclaurin's theorem.
def cos(x):
    res = 0
    circle = (2*3.141592653589)             # Variable used to check if the angle is bigger than 360 degrees.
    if x > circle:
        n = (x % circle)                    # If so then it uses the remainder as the new angle.
    else:
        n = x
    # The more iterations of the function, the more accurate the result will be. 85 used because it is the maximum
    # amount of iterations this machine can handle.
    for i in range(85):
        num1 = (-1)**i
        num2 = n**(2*i)
        num3 = float(num1*num2)
        num4 = float(fact(i*2))
        num5 = num3/num4
        res = res + num5
    return res


# Input in radians.
print(cos(90))

# Algorithm only accurate up to 10 decimal places.
