def find_CH(word, ch, pos):
    
        if ch in word[pos:]:
            print("present")
        else:
            print("Not present")

word = input("Enter the word of your choice: ")
ch = input("Enter the character you want to search: ")
if ch in word:
    pos = int(input("Enter the position you want to start searching: "))
    find_CH(word, ch, pos)
else:
    print("Character not present in the string")
