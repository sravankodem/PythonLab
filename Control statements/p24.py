#Program 24: A Python program to display numbers from 10 to 6 and br when the number about to display is 5.

# Using break to come out of while loop
x=10
while x>=1:
    print ('x=', x)
    x-=1
    if x==5:
        break
print("out of loop")
    
