def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))

num_str = str(num)

sum_of_factorials = sum(factorial(int(digit)) for digit in num_str)

if sum_of_factorials == num:
    print(num, "is a strong number.")
else:
    print(num, "is not a strong number.")
