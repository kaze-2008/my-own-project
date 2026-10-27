a=int(input())
lst=[]
for k in range(1,a+1):
    if k%3==0:
        lst.append(k)
print(len(lst))