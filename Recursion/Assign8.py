"""     recursive function to calculate sum of first N odd natural numbers      """
def addOdd(n):
    if n==1:
        return 1
    return (n*2-1)+addOdd(n-1)

print(addOdd(5))