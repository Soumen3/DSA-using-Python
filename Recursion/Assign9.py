"""   recursive function to calculate sum of first N even natural numbers       """
def addEven(n):
    if n==1:
        return 2
    return n*2 + (addEven(n-1))

print(addEven(5))