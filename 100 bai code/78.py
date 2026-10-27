a=input()
a=a.lower()
lst=[]
dem=[]
for k in a:
    if k not in lst:
        lst.append(k)
for k in lst:
    dem.append(a.count(k))
for k in range(len(lst)):
    print(f"{lst[k]}:{dem[k]}",end=" ")