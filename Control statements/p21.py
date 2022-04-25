#Program 21: A Python program to display the stars in an equilateral triangular form

# to display stars in equilateral triangular form 
n=40
for i in range (1, 11):
    print(''*n, end='') # repeat space for n times
    print('*' *(i)) # repeat star for i times
    n-=1
