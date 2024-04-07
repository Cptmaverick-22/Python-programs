def pallindrome(l):

    if l.lower()[::-1] == l.lower():
        print('True')
    else:
        print('False')

l = input("Enter a string: ")
pallindrome(l)
