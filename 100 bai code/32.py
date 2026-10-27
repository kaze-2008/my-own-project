a,b=map(int,input().split())
check=0
sum_even=0
for k in range(a,b+1):
    if k%3==0 or k%5==0:
        check+=1
    if k%2==0:
        sum_even+=k
print(f"{check} {sum_even}")