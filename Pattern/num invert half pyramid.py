def pattern(row):
    for i in range(row,0,-1):
        for j in range(1,i+1):
            print(i,end='')
        print()

row = int (input("Enter the row number: "))
pattern(row)