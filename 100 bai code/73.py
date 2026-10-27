a=input()
lst=[]
for k in a:
    if k==" ":
        lst.append(k)
    else:
        lst.append(k.lower())
for k in lst:
    print(k,end="")