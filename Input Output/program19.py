#Program 19: A Python program to find the sum of even numbers using command line

# read command line arguments except the program nameto find sum of even numbers

import sys

args = sys.argv[1:]

print (args)

sum=0

# find sum of even arguments

for a in args:
    x = int(a)
    if x%2==0:
        sum+=x
print('Sum of evens = ',sum)

