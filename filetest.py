fname = input("Enter file name: ")
file = open(fname,"r")
for i in file:
    print(file.readline())

