n = int(input("Enter the table you would like to print: "))
i = int(input("Enter the range of the table: "))
for t in range(1, i + 1):
    print(f"{n} * {t} = {n * t}\n")
