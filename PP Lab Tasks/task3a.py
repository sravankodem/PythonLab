fname = input("Enter file name: ")
fh = open(fname)
print(type(fh))
data=fh.readline()
print(type(data))
#data.sort()
print(data)
for i in data:
  print(i)
