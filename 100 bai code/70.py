a=input()
up=True
lst=[]
for k in range(len(a)):
    if a[k]!=" " and up==True:
        lst.append(a[k].upper())
        up=False
    elif a[k]==" ":
        lst.append(" ")
        up=True
    else:
        lst.append(a[k])
for k in lst:
    print(k,end="")