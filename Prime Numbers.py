num = int(input("Enter any number: "))

if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % 1 == 0:
            print(f"{num} is not a prime number")
            break

    else:
        print(f"{num} is a prime number")
else:
     print(f"{num} is not a prime number")