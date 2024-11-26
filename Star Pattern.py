n = int(input("Enter the Number of Rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end= "  ")

    print()    