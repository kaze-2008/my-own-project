a=input()
lst=[]
for k in range(len(a)-1,-1,-1):
    lst.append(a[k])
if lst==list(a):
    print("Yes")
else:
    print("NO")