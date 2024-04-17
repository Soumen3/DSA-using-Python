"""     recursive function to calculate sum of squares of first N natural numbers.     """
def addSquare(n):
    if n == 0:
        return 0
    return n**2 + addSquare(n-1)

print(addSquare(4))