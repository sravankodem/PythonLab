#Program 17: A Python program to display command line arguments. # to display command line args. Save this as cmd.py. import sys
import sys
n = len(sys.argv)
args = sys.argv # n is the number of arguments

#args list contains arguments

print('No. of command line args= ', n)
print('The args are: ', args)
print('The args one by one: ')
for a in args:
      print (a)
