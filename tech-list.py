n=int(input())
x=[]
for i in range(n):
    a=list(input().split())
    if a[0]=='1':
        x.append(a[1])
    elif a[0]=='2':
        print(x)
