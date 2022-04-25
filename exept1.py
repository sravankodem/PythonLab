

fname=input("enter file name")
try:
    f=open(fname)
except Exception:
    print("File Not exist")
else:
    x=f.readlines()
    print(x)   

