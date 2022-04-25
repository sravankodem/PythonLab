n=int(input())
z=[]
for i in range(n):
    x,y=map(int,input().split())#you can change the int to specify or intialize any other data structures
    if x==1:
        z.append(y)
print(z)



