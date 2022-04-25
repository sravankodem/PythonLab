#Program 22: A Python program to find the power value of a number when it is raised to a to find power value of a number. Save this as args.py

import argparse

# call the ArgumentParser()
parser = argparse. ArgumentParser()
# add the arguments to the parser

parser.add_argument('nums', nargs=2)

# retrieve the arguments into args object

args = parser.parse_args()

# find the power value

# args.nums represents a list
print('Number=', args.nums [0])

print('Its power= ', args.nums [1])

#sunvert the arguments into float and then find power

result = float(args.nums [0])** float(args.nums [1])

print('Result=', result)
