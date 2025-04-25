def pattern(row):
    for i in range(1,row+1):
        for k in range(row-i,0,-1):
            print("  ",end='')
        for j in range(i,i*2):
            print(j,end=' ')
        for l in range(i*2-2,i-1,-1):
            print(l,end=' ')
        # s
        print()

row = int(input("Enter the row number: "))
pattern(row)