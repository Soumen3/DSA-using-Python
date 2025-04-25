def pattern(row, column):
    for i in range(row):
        for j in range(column):
            if (i==0 or i==row-1) or (j==0 or j==column-1):
                print("*",end='')
            else:print(" ",end='')
            

        print()        

row, column= int(input("Enter the row number: ")), int (input("Enter the column number: "))
pattern(row, column)