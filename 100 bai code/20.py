a=int(input())
lst=[]
if a//5000!=0:
    lst.append(a//5000)
    a=a-a//5000*5000
if a//2000!=0:
    lst.append(a//2000)
    a=a-a//2000*2000
lst.append(a//1000)
for k in lst:
    print(k,end=" ")