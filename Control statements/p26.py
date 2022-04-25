#Program 26: A program to know that pass does nothing.

# Using pass to do nothing
x = 0
while x<10:
    x+=1
    if x>5: # if x > 5 then continue next iteration
        pass
    print ('x= ',x)

print ("Out of loop")
