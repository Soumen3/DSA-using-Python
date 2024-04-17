"""     Print first N even natural number in  reverser    """

def printOdd(n):
    if n <= 0 :
        return
    print(n*2, end=' ')
    printOdd(n-1)

printOdd(10)