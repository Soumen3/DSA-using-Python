def pattern(row, column):
    for i in range(row):
        for j in range(column):
            print("* ",end="")
        print()


row,column=int(input("Enter the row numbeer: ")), int (input("Enter the column number: "))
pattern(row, column)