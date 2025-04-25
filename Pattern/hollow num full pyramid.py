def pattern(row):
    for i in range(1,row+1):
        for k in range(row, i,-1):
            print(" ",end='')

        for j in range(1,i+1):
            if i==row:
                print(j,end=' ')
            elif j==1:
                print(j,end='')
                
            else:
                print(' ',end='')
        
        for j in range(1,i):
            if j==i-1 and j<row-1:
                print(j+1,end='')
            else:
                print(" ",end='')                
            
        print()

row = int(input("Enter the row number: "))
pattern(row)