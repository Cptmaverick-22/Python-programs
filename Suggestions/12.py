rows = int(input("Enter number of rows: "))
max_width = len(' '.join(map(str, range(1, rows + 1))))

for i in range(1, rows + 1):
    numbers = ' '.join(map(str, range(1, i + 1)))
    spaces = ' ' * ((max_width - len(numbers)) // 2)
    print(spaces + numbers)
