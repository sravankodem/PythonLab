n=int(input())
pair = []

for i in range(0,n):
        x=[]
        word = input().split()
        x.append(word)
        value = int(word[1])
        x.append(value)
        pair.append(x)

print(pair)
