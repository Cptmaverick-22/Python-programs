def leap(x):
    if (x%4==0 and x%100!=0) or x%400==0:
        print("Leap year")
    else:
        print("Not a leap year")
x= int(input("Enter a year: "))
leap(x)