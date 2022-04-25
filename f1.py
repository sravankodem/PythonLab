
fname = input("Enter file name: ")
fh = open(fname)
data=fh.readlines()
data.sort()
for i in range(len(data)):
    print(data[i])
