fname = input("Enter file name: ")
words=0
char=0
lines=0
fh = open(fname)
#print(word)
#word.sort()
for i in fh:
    print(i)
    lines+=1
    words+=len(i)
    line=i.split()
    char+=len(line)
print(lines,char,words)
