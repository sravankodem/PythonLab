person = [ ]
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = [input(), int(input())]
    person.append(ele)
print("list before sorting")
print(person)

b=sorted(person, key=lambda u: u[1])
print("list sorted according to age")
print(b)

b=sorted(person, key=lambda u: u[0])
print("list sorted according to Name")
print(b)


