def main():
    lst = []
    count = 0
    for i in range(int(input())):
        lst.append(input())
    for i in lst:
        if(lst.count(i) == 1):
            count+=1
    print(count)

main()
