name = input("Enter a string: ")
ch = input("Enter a character: ")
for i in name:
    if(ch == i):
        print("present")
        break
else:
    print("Absent")

