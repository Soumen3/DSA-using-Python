"""     Print first N natural numbers       """

def printN(n):
    if n==1:
        print(n, end=' ')
        return
    printN(n-1)
    print(n, end=' ')

printN(10)