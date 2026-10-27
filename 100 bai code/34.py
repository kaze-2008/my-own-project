a,b=map(int,input().split())
element=[]
for k in range(a,b+1):
    lst=0
    for i in range(1,k+1):
        if k%i==0:
            lst+=1
    if lst==2:
        element.append(k)
for k in element:
    print(k,end=" ")