empty_tuple = () 
print (empty_tuple)
tup = 'python', 'lab'
print(tup)
tup = ('Second Year', 'Second Semister') 
print(tup)
	# Code for concatenating 2 tuples 
tuple1 = (0, 1, 2, 3) 
tuple2 = ('python', 'lab') 
	 # Concatenating above two
print('Concatenating tuples')
print(tuple1 + tuple2)
	# Code for creating nested tuples 
tuple1 = (0, 1, 2, 3) 
tuple2 = ('python', 'lab') 
tuple3 = (tuple1, tuple2)
print('Nested tuples')
print(tuple3)
	# Code to create a tuple with repetition 
tuple3 = ('python',)*3
print('Tuple created with repetitions')
print(tuple3)
	# code to test slicing 
tuple1 = (0 ,1, 2, 3)
print('Slicing Tuples')
print(tuple1[1:]) 
print(tuple1[::-1]) 
print(tuple1[2:4])
	# Code for printing the length of a tuple 
tuple2 = ('python', 'lab')
print('length of tuple')
print(len(tuple2))
	# Code for converting a list and a string into a tuple 
list1 = [0, 1, 2]
print('Conversion of list into python')
print(tuple(list1)) 
print(tuple('python')) # string 'python'
