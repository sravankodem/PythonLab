#Program 22: A Python program to display numbers from 1 to 100 in a proper format.
# Displaying numbers from 1 to 100 in 10 rows and 10 cols.

for x in range (1, 11):
    for y in range(1, 11):
        print('{:8}'. format (x*y), end='') # each column size is 8
    print()
