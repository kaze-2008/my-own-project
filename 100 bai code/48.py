a=int(input())
lst=list(map(int,input().split()))
mod5=[]
for k in lst:
    if k%5==0:
        mod5.append(k)
if len(mod5)==0:
    print("-")
else:
    for k in mod5:
        print(k, end=" ")
    print(f"\n{sum(k for k in mod5)}")