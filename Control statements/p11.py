#Program 11: A Python program to display even numbers between m and n.
# to display even numbers between m and n
m, n =[int(i) for i in input("Enter minimum and maximum range:").split(',')]
x=m
if x % 2 !=0 : # if x is not even, start from next number
    x=x+1   # start from m onwar

while x>=m and x<=n:
      print(x)
      x+=2
