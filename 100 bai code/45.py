a=int(input())
lst=list(map(int,input().split()))
sm=0
even=False
for k in lst:
    if k%2==0:
        sm+=k
        even=True
if even==False:
    print("-")
else:
    print(sm)