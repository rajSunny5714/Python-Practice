num = int(input("Enter a number: "))

if num == 0:
    print("Binary:", 0)
else:
    binary = ""

    while num > 0:
        binary = str(num % 2) + binary
        num //= 2

    print("Binary:", binary)