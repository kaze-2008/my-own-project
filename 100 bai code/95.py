a=int(input())
b=list(map(int,input().split()))
def sum(x):
    sm=0
    for k in x:
        sm+=k
    return sm
print(f"{sum(b)/a:.1f}")