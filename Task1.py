# Method grabs values from an array and tries different combinations to find two pairs that ave the same product.
# Grabs first element, grabs one after it, takes another after the first, that is not equal to the second, the takes one
# after the third that is also not equal to the second, multiplies them separately and prints them if they have an equal
# product. Thus avoiding different permutations of the same answer.


def pairs(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(i+1, len(arr)):
                if arr[k] != arr[j]:
                    for m in range(k+1, len(arr)):
                        if arr[m] != arr[j]:
                            if (arr[i]*arr[j]) == (arr[k]*arr[m]):
                                print("%d x %d = %d x %d = %d" % (arr[i], arr[j], arr[k], arr[m], (arr[k]*arr[m])))


varx = list(range(1, 11))
pairs(varx)

# Completely inefficient method. Another method would be to have an object that takes 2 integers and their product.
# Create an array of said objects using the list of numbers, and then using the same method in task 6, remove the
# objects from the list that have unique product value, then just print different combinations of the resulting array of
# objects with repeated product value.
