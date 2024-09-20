def print_diamond(n):
    for i in range(n // 2 + 1):
        print(' ' * (n // 2 - i) + '*' * (2 * i + 1))
    for i in range(n // 2 - 1, -1, -1):
        print(' ' * (n // 2 - i) + '*' * (2 * i + 1))


while True:
    n = int(input("Enter the size of the diamond: "))
    if n % 2 != 0:
        print_diamond(n)
        break
    else:
        print("Please provide an odd integer.\n")
