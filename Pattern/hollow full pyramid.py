def pattern(row):
    for i in range(row):
        for k in range(row-i-1):
            print(" ",end='')
        
        for j in range(i+1):
            if i<=1 or i==row-1 or j==0 or j==i:
                print("* ",end='')
            else: print("  ", end='')
    
        print()

row = int (input("Enter the row:"))
pattern(row)