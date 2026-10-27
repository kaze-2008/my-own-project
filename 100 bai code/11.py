a=int(input())
lst=[]
while a!=0:
    lst.append(a-(a//60)*60)
    a=a//60
lst.reverse()
for k in lst:
    if k !=lst[len(lst)-1]:
        print(k,end=":")
    else:
        print(k)