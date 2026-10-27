k,x=map(int,input().split())
def f(a,n):
    c=x
    return a*(c**n)
sm=0
for i in range(k):
    a,n=map(int,input().split())
    sm+=f(a,n)
print(sm)