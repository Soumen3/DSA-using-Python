def pattern(row):
    for i in range(row,0,-1):
        for j in range(i):
            print('*',end='')

        print()

row= eval(input("enter the row number: "))
pattern(row)