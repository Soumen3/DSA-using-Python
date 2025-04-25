"""     Print first N odd natural number       """

def printOdd(n):
    if n <= 0 :
        return
    printOdd(n-1)
    print(n*2-1, end=' ')

printOdd(10)