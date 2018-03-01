def prime(n):
    arr = list(range(2, n + 1))
    for x in range(int(n**0.5)):
        for i in arr:
            if arr[x] == i:
                None
            elif (i % arr[x]) == 0:
                arr.remove(i)
    return arr


def IsPrime(n):
    for x in range(2, n):
        if n % x == 0 and n != x:
            return False
    return True


UserInput = input("Enter a number to find all the prime number up to it\n")
print("Prime Numbers: \n%s" % prime(UserInput))
User2 = input("Enter a number to check if it's prime\n")
print(IsPrime(User2))
