
x=int(input())
##
##k=5//x
##
##print(k)
try:
    k = 5 // x # raises divide by zero exception.
    print(k)

# handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    # this block is always executed
    print('This is always executed')
