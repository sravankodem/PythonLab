num = int(input("Enter a number: "))
factorial = 1
    # check if the number is negative, positive or zero
for i in range(1,num + 1):
    factorial = factorial*i
print("The factorial of",num,"is",factorial)
