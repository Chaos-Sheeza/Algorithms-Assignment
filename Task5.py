# a function that finds the closest guess to the root
def guess(num):
    if num > 100:
        n = num                 # n for temporary storage of the number.
        i = 0                   # i to store how much the decimal point has moved.
        # While n is bigger than 100, it increments i,  then divides the number by 10^i. Once the number is smaller than
        # 100, checks if i is an even number (i needs to be even since everytime a number is squared their '0's are
        # multiplied by 2), if not i-1, and sets another temporary variable (num1) to the number divided by 10^i.
        while n > 100:
            i += 1
            n = num/(10**i)
        if i % 2 != 0:
            i = i-1
        num1 = num/(10**i)
    # If number is smaller then 1 then the same algorithm is applied, but every time i is decreased by 1, and if it is
    # not even by the end it is incremented by 1.
    elif num < 1:
        n = num
        i = 0
        while n < 1:
            n = num/(10**i)
            i -= 1
        if i % 2 != 0:
            i = i+1
        num1 = num/(10**i)
    # Otherwise it sets i as default value 0 and the temporary variable is set to the original number.
    else:
        i = 0
        num1 = num
    # Algorithm squares every whole number up to the variable until it finds the closest square to the variable.
    for x in range(int(num1)):
        y = x**2
        # If y is equal to num1 then the square root has been found immediately and returns x.
        # Else compares the the current square and the previous one by subtracting from the input, the smallest number
        # is chosen (since it's obviously closer).
        # Before returning the variable, it moves the decimal point according to the algorithms used before.
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
    # Created to handle imaginary numbers, just switches number from negative to positive and calls function again, then
    # prints an i at the end.
    elif n < 0:
        return '(' + str(sqrt(-n)) + ')i'
    else:
        n1 = guess(n)
    # Basically using the babylonian method, grab the number, divide it by the guess, add the result to the guess and
    # divide by 2. Keep using the result as the new guess. The more time it loops the more accurate the answer is.
    # A counter was added to optimise algorithm.
    count = 0
    for i in range(6):
        y = float(n/n1)
        n1 = float((y+n1)/2)
        '''
        if y == n1:
            count += 1
        if count == 3:
            break
        '''
    return n1


print(sqrt(225252425424251984552))
