a=input()
for k in range(len(a)-1,-1,-1):
    if a[k]!="+":
        a=a[:k+1]
        break
for k in a:
    print(k,end="")