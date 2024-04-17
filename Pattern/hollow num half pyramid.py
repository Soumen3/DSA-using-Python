def pattern(row):
    for i in range(1,row+1):
        for j in range(1,i+1):
            if i==row or i==1 or j==1 or j==i:
                print(j,end=' ')
            else:print('  ',end='')
        print()

row = int(input("Enter the row number: "))
pattern(row)