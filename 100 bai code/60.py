import math
a=list(map(int,input().split()))
check=[]
for k in a:
    if k>0 and int(math.sqrt(k))**2==k:
        check.append(k)
if len(check)==0:
    print("-")
else:
    print(f"{sum(k for k in check)/len(check):.1f}")