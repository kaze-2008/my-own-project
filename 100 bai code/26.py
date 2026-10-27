a=int(input())
lst=[]
for k in range(1,a+1):
    if k%15==0:
        lst.append(k)
print(sum(k for k in lst))