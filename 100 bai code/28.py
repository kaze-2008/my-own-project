a=int(input())
lst=0
for k in range(1,a+1):
    if a%k==0:
        lst+=1
print(lst)