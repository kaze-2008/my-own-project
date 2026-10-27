import math
a=list(map(int,input().split()))
def check_cp(x):
    cp=[]
    for k in x:
        if k>=0:
            b=math.sqrt(k)
            if int(b)**2==k:
                cp.append(k)
    return cp
cp=check_cp(a)
print(f"{sum(k for k in cp)/len(cp):.1f}")