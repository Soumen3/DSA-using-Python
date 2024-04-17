def pattern(row):
    space=row//2
    for i in range(row):
        for k in range(row-i-1):
            print(" ", end='')
        for j in range(i+1):
            print("* ", end='')
        
        print()

row = int(input("enter the row number: "))
pattern(row)