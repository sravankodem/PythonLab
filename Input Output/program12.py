#Program 12: A Python program to accept 3 integers separated by commas and display their sum.

# 3 numbers separated by comma.

varl, var2, var3 = [int(x) for x in input("Enter three numbers:").split(',')]

print("Sum = ", varl+var2+var3)
