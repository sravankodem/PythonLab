#Program 18: A Python program to display and sum of a list of numbers usi # to find sum of a list of numbers using while - v2.0

# take a list of numbers

list = [10,20,30,40,50]

sum=0 #initially sum is zero 
i=0 #take a variable

while i <len (list):
    print(list[i]) #display the element from list
    sum+=list[i] #add each element to su
    i+=1
print('Sum= ', sum)
