def reverse_string(string):
    l=list(string)
    occ={}
    for x in l:
       occ[x]=string.count(x)

    x=dict(sorted(occ.items(), key=lambda item: item[1]))
    c=[]
    y=""
    for key in x:
        y=y+(key+str(x[key]))
    '''for key in c:
        y=y+key'''
    return y
        
x=input()
print(reverse_string(x))


'''cco=list(reversed(occ))
for x in cco:
    print(x,end='')
    print(occ[x],end='')'''
    
