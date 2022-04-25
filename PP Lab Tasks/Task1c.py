
n=int(input())
matrix = []

for i in range(n):
   row = list(input().split())
   row[1]=int(row[1])
   matrix.append(row)

b=sorted(matrix, key=lambda u: u[1])
print("list sorted according to age")
print(b)
