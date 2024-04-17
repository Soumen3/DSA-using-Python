def pattern(row):
    for i in range(1,row+1):
        for j in range(1,i+1):
            print(j,end='')
        
        print()

row = int (input("Enter the row: "))
pattern(row)