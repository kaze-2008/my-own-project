a=int(input())
lst=list(map(int,input().split()))
sm=0
for k in range(a):
    if k%2==0:
        sm+=lst[k]
print(sm)