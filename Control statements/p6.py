#Program 6: A Python program to test whether a given number is in between 1 and 10

# using and in if else statement 
x = int(input('Enter a number: '))
if x>=1 and x<=10:
        print("You typed", x, "which is between 1 and 10")
else:
    print("You typed", x, "which is below 1 or above 10")
