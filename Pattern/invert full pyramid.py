def pattern(row):
    for i in range(row,0,-1):
        for k in range(row-i):
            print(" ",end='')
        for j in range(i):
            print("* ",end='')
        print()

row = int (input("Enter the row number: "))
pattern(row)