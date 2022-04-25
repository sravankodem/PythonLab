	#Creating a Dictionary with Integer Keys 
Dict = {1: 'Python', 2: 'Lab', 3: 'CSE'} 
print("\nDictionary with the use of Integer Keys: ") 
print(Dict) 
	# Creating a Dictionary with Mixed keys 
Dict = {'Name': 'Python Lab', 1: [1, 2, 3, 4]} 
print("\nDictionary with the use of Mixed Keys: ") 
print(Dict)
	# Creating an empty Dictionary 
Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 
	# Creating a Dictionary with dict() method 
Dict = dict({1: 'Python', 2: 'Lab', 3: 'CSE'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict) 
	# Creating a Dictionary with each item as a Pair 
Dict = dict([(1, 'Python'), (2, 'Lab')]) 
print("\nDictionary with each item as a pair: ") 
print(Dict)
	# Creating a Nested Dictionary  
Dict = {1: 'Python', 2: 'Lab', 3:{'A' : 'NewLab', 'B' : 'IN', 'C' : 'GR20'}} 
print(Dict)
	# Python program to demonstrate accessing a element from a Dictionary  
	# Creating a Dictionary  
Dict = {1: 'Python', 'name': 'Lab', 3: 'CSE'} 
	# accessing a element using key 
print("Accessing a element using key:") 
print(Dict['name']) 
	# accessing a element using key 
print("Accessing a element using key:") 
print(Dict[1]) 
	# Creating a Dictionary  
Dict = {1: 'Python', 2: 'Lab', 3: 'CSE'} 
	# accessing a element using get() method 
print("Accessing a element using get:") 
print(Dict.get(3))
	# Creating a Dictionary 
Dict = {'Dict1': {1: 'PythonLab'}, 'Dict2': {'Name': 'CSE'}} 
	# Accessing element using key 
print(Dict['Dict1']) 
print(Dict['Dict1'][1]) 
print(Dict['Dict2']['Name'])
	# Initial Dictionary 
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'CSE', 
        'A' : {1 : 'Python', 2 : 'Lab', 3 : 'Manual'}, 
        'B' : {1 : 'Second Year', 2 : 'Second Semister'}} 
print("Initial Dictionary: ") 
print(Dict) 
	# Deleting a Key value 
del Dict[6] 
print("\nDeleting a specific key: ") 
print(Dict) 
	# Deleting a Key from Nested Dictionary 
del Dict['A'][2] 
print("\nDeleting a key from Nested Dictionary: ") 
print(Dict)
	# Creating a Dictionary 
Dict = {1: 'Lab', 'name': 'For', 3: 'Python'}
	# Deleting entire Dictionary 
Dict.clear() 
print("\nDeleting Entire Dictionary: ") 
print(Dict)
