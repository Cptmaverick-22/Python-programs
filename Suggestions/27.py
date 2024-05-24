def is_even(num):
    return all(int(digit) % 2 == 0 for digit in str(num) )

result = [num for num in range(200, 500+1) if is_even(num)]
print("The even digits number: ",result)
