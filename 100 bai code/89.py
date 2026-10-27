a=int(input())
sm=0
def gt(x):
    a=1
    for k in range(1,x+1):
        a*=k
    return a
def C(n,k):
    return gt(n)/(gt(k)*gt(n-k))
for k in range(a):
    b,c=map(int,input().split())
    sm+=C(b,c)
print(f"{sm:.0f}")