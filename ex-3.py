n=int(input())
pair = dict()

for i in range(0,n):
        word = input().split()
        key = word[0]
        value = int(word[1])
        pair[key]=value

print(pair)

b=sorted(pair.items(), key=lambda u: u[0], reverse=True)
print("list sorted according to age")
print(b)
