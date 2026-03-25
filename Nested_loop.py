rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for x in range(columns):
     print(symbol, end="")
    print()

