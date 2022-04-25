#Program 23: A Python program to search for an element in the list of elements.
# searching for an element in a list 


group1 = [1,2,3,4,5] #take a list of elements 
search= int(input('Enter element to search: '))
for element in group1:
    if search == element:
        print('Element found in group1')
        break # come out of for loop
else:
    print('Element not found in group1') # this is else suite
