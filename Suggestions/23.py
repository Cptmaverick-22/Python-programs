input_string = 'aabbaaacccbabbaa'
char = input("Enter the character to search for longest sub string: ")
current_length = 0
max_length = 0

for c in input_string:
    if c == char:
        current_length+=1
        max_length = max(current_length, max_length)
    else:
        current_length = 0

print(f"The longest substring of {char} is: {max_length}")
