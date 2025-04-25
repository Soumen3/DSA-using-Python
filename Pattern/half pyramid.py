def pattern(row):
    for i in range(row):
        for j in range(i+1):
            print("*", end='')
        print()
    
row= int (input("Enter the row: "))
pattern(row)