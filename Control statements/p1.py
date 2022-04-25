#Program 1: A Python program to calculate the area of a circle.

# to find area of a circle

import math #here math module is imported 
r = float(input('Enter radius: '))
area = math.pi* r**2 #pi is a constant in math module

print('Area of circle=1', area) 
print('Area of circle= {:0.2f}'.format(area))
