lst=list(map(int,input().split()))
element=[]
for k in lst:
    if k>0:
        check=0
        for i in range(1,k+1):
            if k%i==0:
                check+=1
        if check==2:
            element.append(k)
if len(element)==0:
    print("-")
else:
    print(max(element))