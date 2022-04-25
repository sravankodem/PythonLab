#Program 35: Write a Python program to calculate the Sine value of a given angle in degrees by evaluating Sine series.
# program to evaluate Sine series. #accept user input
x, n = [int(i) for i in input ("Enter power of e , no. of iterations: ").split(',')]
# convert the angle from degrees into radians first term

t=1
sum=t # display the iteration number and sum
print('Iteration= %d\tSum= %f' %(1, sum))
for j in range (1, n):
    t= t* x/j # find the next term
    sum=sum+t; # add it to sum
    print('Iteration= %d\tSum= %f '%(j+1,sum))
