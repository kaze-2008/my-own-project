a=input()
lst=[]
for k in a:
    if k==" ":
        lst.append(k)
    else:
        lst.append(k.upper())
for k in lst:
    print(k,end="")