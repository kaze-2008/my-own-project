a=list(map(int,input().split()))
def element(x):
    element=[]
    for k in x:
        lst=0
        for i in range(1,k+1):
            if k%i==0:
                lst+=1
        if lst==2:
            element.append(k)
    return element
lst=element(a)
print(f"{sum(k for k in lst)/len(lst):.2f}")