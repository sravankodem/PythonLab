#Program 34: Write a Python program to calculate the Sine value of a given angle in degrees by evaluating Sine series.
# program to evaluate Sine series. #accept user input
x, n = [int(i) for i in input ("Enter angle value, no. of iterations: ").split(',')]
# convert the angle from degrees into radians first term

r=(x*3.14159)/180
t=1
sum=1 # display the iteration number and sum
print('Iteration= %d\tSum= %f % (1, sum)')
i=1
for j in range (2, n+1):
    t=(-1)*t*r*r/(i*(1+1)) # find the next term
    sum=sum+t; # add it to sum
    print('Iteration= %d\tSum= %f '%(j,sum))
    i+=2
