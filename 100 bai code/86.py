import math
a,b,c=map(int,input().split())
def cv():
    return a+b+c
p=cv()/2
def s():
    return math.sqrt(p*(p-a)*(p-b)*(p-c))
print(f"{cv():.1f} {s():.3f}")