def pattern(row):
    for i in range(row,0, -1):
        for j in range(i):
            if i==row or i <=2 or j==0 or j==i-1:
                print("*",end='')
            else: print(' ',end='')
        print()

row = int (input("Enter the row number: "))
pattern(row)