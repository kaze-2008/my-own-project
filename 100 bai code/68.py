a=input()
Space=[]
lst=[]
for k in range(len(a)-1):
    if a[k]!=" ":
        a=a[k:]
        break
    Space.append(" ")
lst=a.split()
result=" ".join(lst)
for k in Space:
    print(k,end="")
print(result)    