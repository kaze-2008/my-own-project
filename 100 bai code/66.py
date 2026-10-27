a=input()
for k in range(len(a)-1):
    if a[k]!=" ":
        a=a[k:]
        break
for k in a:
    print(k,end="")