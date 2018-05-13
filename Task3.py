# Function that outputs list of prime numbers up to n.


# Creates a list from 2 to n, and loop size square root of n (where n is the size of the list). Then divides every
# element of the list by every number removing every element that does not have a remainder.
def prime(n):
    arr = list(range(2, n + 1))
    for x in range(int(n**0.5)):
        for i in arr:
            # Added so that first prime found is not removed
            if arr[x] == i:
                None
            elif (i % arr[x]) == 0:
                arr.remove(i)
    return arr


# Boolean function to check whether a number is prime.
# Divides n by every number from 2 and if one does not return a remainder, then the loop is stopped and returns false,
# else it returns true.
def IsPrime(n):
    for x in range(2, n):
        if n % x == 0 and n != x:
            return False
    return True


UserInput = input("Enter a number to find all the prime number up to it\n")
print("Prime Numbers: \n%s" % prime(UserInput))
User2 = input("Enter a number to check if it's prime\n")
print(IsPrime(User2))
