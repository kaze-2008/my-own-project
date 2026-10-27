a=list(map(int,input().split()))
lst=[]
for k in a:
    if k<0:
        lst.append(k)
if len(lst)==0:
    print("-")
else:
    print(max(lst))