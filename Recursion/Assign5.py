"""     Print first N odd natural number in reverse   """

def printOdd(n):
    if n <= 0 :
        return
    print(n*2-1, end=' ')
    printOdd(n-1)

printOdd(10)