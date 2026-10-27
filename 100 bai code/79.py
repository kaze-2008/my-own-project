a=input()
a=a.lower()
lst=[]
dem=[]
for k in a:
    if k not in lst and k!=" ":
        lst.append(k)
for k in lst:
    dem.append(a.count(k))
letter=max(dem)
print(f"{lst[dem.index(letter)]}:{letter}")