n=int(input())
pair = []

for i in range(0,n):
        x=[]
        name,age = input().split()
        age=int(age)
        x.append(name)
        x.append(age)
        pair.append(x)


print(pair)
print(sorted(pair,key= lambda u:u[1]))
