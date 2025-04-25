"""     Print first N even natural number       """

def printOdd(n):
    if n <= 0 :
        return
    printOdd(n-1)
    print(n*2, end=' ')

printOdd(10)