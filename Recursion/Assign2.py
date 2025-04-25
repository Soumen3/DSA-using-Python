"""     Print first N natural numbers in reverse       """

def printN(n):
    if n==1:
        print(n, end=' ')
        return
    print(n, end=' ')
    printN(n-1)

printN(10)