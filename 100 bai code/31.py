a,b=map(int,input().split())
check=0
for k in range(a,b+1):
    if k%3==0:
        check+=1
print(check)