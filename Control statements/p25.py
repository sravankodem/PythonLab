#Program 25: A Python program to display numbers from 1 to 5 using continue

# Using continue to execute next iteration of while loop
x=0
while x<10:
    x+=1
    if x>5:
        continue
    print('x= ',x)
print("out of loop")

