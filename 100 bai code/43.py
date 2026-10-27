a=int(input())
lst=list(map(int,input().split()))
i=0
for k in lst:
    if k%2==0:
        i+=1
print(i)