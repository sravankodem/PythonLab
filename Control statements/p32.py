#Program 32: Write a Python program to display prime number series.

#program to print prime numbers upto a given number
#accept upto what number the user wants

max = int(input ("Upto what number? "))
for num in range (2, max+1): # generate from 2 onwards till max
    for i in range (2, num): # i represents numbers from 2 to num-1
        if (num % i) == 0: # if num is divisible by i
            break # it is not prime, hence go back and check next num
    else:
        print (num) # otherwise it is prime and hence display

